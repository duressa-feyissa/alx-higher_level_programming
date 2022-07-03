#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  prints some basic info about Python lists.
 *
 * @p: PyObject as argument
 * Return: Void
 */
void print_python_list_info(PyObject *p)
{
	long int len, i;
	PyListObject *abc;

	len = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", len);

	abc = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", abc->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(abc, i);
		printf("Element %ld: %s\n", i, Py_TYPE(abc)->tp_name);
	}
}
