#include <Python.h>


/**
 * print_python_list_info -  prints some basic info about Python lists.
 * @p: python object
 */

void print_python_list_info(PyObject *p)
{
	long int size_1 = PyList_Size(p);
