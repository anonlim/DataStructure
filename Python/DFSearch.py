from GraphType import *

def depth_first_search(graph, startVertex, endVertex):
    stack = StackType()
    vertexQ = QueType()
    found = False

    '''[9]'''
    graph.clear_marks()
    stack.push(startVertex)


    while True:
        vertex = stack.top()
        stack.pop()
        if vertex == endVertex:
            print(vertex)
            found = True
        else:
            if graph.is_marked(vertex) is not True:
                graph.mark_vertex(vertex)
                print(vertex)
                graph.get_to_vertices(vertex, vertexQ)
                while vertexQ.is_empty() is not True:
                    item = vertexQ.dequeue()
                    if (graph.is_marked(item) is not True):
                        stack.push(item)
        if stack.is_empty()is False and found is False:
            continue
        break

    if found is False:
        print("Path not found")
