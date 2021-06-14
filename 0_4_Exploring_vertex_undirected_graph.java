// undiretced graph
import java.util.*;
public class Exploring{
    private int ver;
    private boolean[] visited;
    private List<Integer> adjList[];
    // constructor for the adjacency list
    Exploring(int v){
        ver = v;
        visited = new boolean[v];
        adjList = new ArrayList[v];
        for (int x = 0; x<v; x++){
            //  create the list for all for the vertices conneected to it
            adjList[x] = new ArrayList();
            //  checking for the key whether visited or not
            visited[x] = false;
        }
    }

    // exploring the given vertex
    void Explore(int ver){
        // making the seen vertex as true
        visited[ver] = true;

        // now iteration through all vertex
        Iterator<Integer> i = adjList[ver].listIterator();
        while(i.hasNext()){
            int vertex = i.next();
            if (visited[vertex]==false){
                Explore(vertex);
            }
        }
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        // vertices
        int ver = scanner.nextInt();
        // edges number
        int edge = scanner.nextInt();

        //  make object of class Exploring  object name is the graph
        Exploring graph = new Exploring(ver);

        // have the edge now
        for (int x = 0; x<edge; x++){
            int ver1 = scanner.nextInt();
            int ver2 = scanner.nextInt();
            //  as it is undirected grapg so we have take care of both the direction
            graph.adjList[ver1].add(ver2);
            graph.adjList[ver2].add(ver1);
        }

        // for the Exploring vertex
        int key = scanner.nextInt();
        scanner.close();

        // testing for correction
        // for (int x=0; x<ver; x++)System.out.print(graph.adjList[x]);
        graph.Explore(key);

        // now print the all vertex from visisted array and see
        for(int x =0; x<ver; x++)System.out.print(x+"-->"+graph.visited[x]+'\t');
    }
}
