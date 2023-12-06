#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < 10 && i < size; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("[.] Size of the Python List = 0\n");
        printf("[.] Allocated = 0\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        } else if (PyTuple_Check(element)) {
            printf("tuple\n");
        } else if (PyList_Check(element)) {
            printf("list\n");
        } else if (PyFloat_Check(element)) {
            printf("float\n");
        } else if (PyLong_Check(element)) {
            printf("int\n");
        } else if (PyUnicode_Check(element)) {
            printf("str\n");
        }
    }
}
