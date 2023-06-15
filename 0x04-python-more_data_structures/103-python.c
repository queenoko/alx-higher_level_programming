#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - basic info of python
 * @p: PyObject list object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, z, lmit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		lmit = 10;
	else
		lmit = size + 1;

	printf("  first %ld bytes:", lmit);

	for (z = 0; z < lmit; z++)
		if (string[z] >= 0)
			printf(" %02x", string[z]);
		else
			printf(" %02x", 256 + string[z]);

	printf("\n");
}

/**
 * print_python_list - prints list info
 *
 * @p: Python object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	long int size, z;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python list = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (z = 0; z < size; z++)
	{
		obj = ((PyListObject *)p)->ob_item[z];
		printf("Element %ld: %s\n", z, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
