#include "binary_trees.h"

/**
 * heap_insert - inserts a value into a Max Binary Heap
 * @root: double pointer to the root node of the Heap
 * @value: value store in the node to be inserted
 *
 * Return: pointer to the inserted node, or NULL on failure
 */
heap_t *heap_insert(heap_t **root, int value)
{
    heap_t *node = NULL;

    if (*root == NULL)
    {
        *root = binary_tree_node(NULL, value);
        return *root;
    }

    node = *root;
    while (1)
    {
        if (!node->left)
        {
            node->left = binary_tree_node(node, value);
            return heapify(node->left);
        }
        else if (!node->right)
        {
            node->right = binary_tree_node(node, value);
            return heapify(node->right);
        }
        else
        {
            if (rand() % 2)
                node = node->left;
            else
                node = node->right;
        }
    }
}

/**
 * heapify - fix the Max Binary Heap
 * @node: inserted node
 *
 * Return: pointer to the root node
 */
heap_t *heapify(heap_t *node)
{
    int temp;

    while (node->parent && node->n > node->parent->n)
    {
        temp = node->parent->n;
        node->parent->n = node->n;
        node->n = temp;
        node = node->parent;
    }

    return (node);
}