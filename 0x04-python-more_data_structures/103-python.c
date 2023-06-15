#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - basic info of python list(PyObject *p)
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
	int size, alloc, z;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (z = 0; z < size; z++)
	{
		type = list->ob_item[z]->ob_type->tp_name;
		printf("Element %d: %s\n", z, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[z]);
	}
}

/**
 * print_python_bytes - basic info about python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char z, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.} bytes object info\n");
	if(strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (z = 0; z < size; z++)
	{
		printf("%02hhx", bytes->ob_sval[z]);
		if (z == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
