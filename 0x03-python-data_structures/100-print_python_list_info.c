#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info -  prints some basic info about Python lists.
 * @p: python object
 */

void print_python_list_info(PyObject *p)
{
	long int size_1 = PyList_Size(p);
	int z;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (z = 0; z < size_1; z++)
		printf("Element %z: %s\n", z, Py_TYPE(obj->ob_item[z])->tp_name);
}
