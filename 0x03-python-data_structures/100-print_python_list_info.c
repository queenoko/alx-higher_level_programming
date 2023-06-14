#include <Python.h>


/**
 * print_python_list_info -  prints some basic info about Python lists.
 * @p: python object
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, z;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (z = 0; z < size; z++)
	{
		printf("Element %d: ", z);

		obj = PyList_GetItem(p, z);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
