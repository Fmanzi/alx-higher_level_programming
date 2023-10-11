#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
Py_ssize_t l_size, s_alloc, i;
PyObject *item;

l_size = PyList_Size(p);
s_alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", l_size);
printf("[*] Allocated = %ld\n", s_alloc);

for (i = 0; i < l_size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
