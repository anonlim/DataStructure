from GraphType import *

def breadth_first_search(graph, startVertex, endVertex):
    queue = QueType()
    vertexQ = QueType()
    found = False

    
    '''[10]'''
    graph.clear_marks()
    queue.enqueue(startVertex)

    while True:
        vertex=queue.dequeue()
        if vertex==endVertex:
            print(vertex)
            found=True
        else:
            if graph.is_marked(vertex) is False:
                graph.mark_vertex(vertex)
                print(vertex)
                graph.get_to_vertices(vertex,vertexQ)

                while(vertexQ.is_empty()is False):
                    item=vertexQ.dequeue()
                    if(graph.is_marked(item)is False):
                        queue.enqueue(item)
        if queue.is_empty()is False and found is False:continue
        else:break

    if found is False:
        print("Path not found")