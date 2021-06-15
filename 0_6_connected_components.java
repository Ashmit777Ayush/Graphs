// undiretced graph
import java.util.*;
public class Connectedcomponenets {
    // vertices
    private int vertices;
    // adjList
    private List<Integer> adjList[];
    // visited
    private boolean visited[];
    // connected comoponenets
    private List<List<Integer>> connectedComp = new ArrayList<>();

    Connectedcomponenets(int v){
        vertices = v;// assign number of vertices
        adjList = new ArrayList[v];// assign adjacency list
        visited = new boolean[v];// visited
        for (int x=0; x<v; x++){
            adjList[x] = new ArrayList();
            visited[x] = false;
        }
    }

    // Explore
    List<Integer> Explore(int vertex, List<Integer> connected){
        //  make the vertex visited
        visited[vertex]=true;
        // add to connected
        connected.add(vertex);

        Iterator<Integer> i = adjList[vertex].listIterator();
        while(i.hasNext()){
            int ver = i.next();
            // check for visited and then explore again
            if (visited[ver]==false){
                Explore(ver, connected);
            }
        }
        return connected;
    }

    // DFS
    void dfs(){
        for(int vertex=0; vertex<vertices; vertex++){
            if (visited[vertex]==false){
                // ceate new connected
                List<Integer> connected = new ArrayList<>();
                Explore(vertex, connected);
                //  addd connected to connectedComp
                connectedComp.add(connected);
            }
        }
    }

    // addEdge
    void addEdge(int vertex1, int vertex2){
        adjList[vertex1].add(vertex2);
        adjList[vertex2].add(vertex1);
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        // vertex and edges of the graph
        int vertex = scanner.nextInt();
        int edges = scanner.nextInt();

        // make object of COnnectedComponents
        Connectedcomponenets graph = new Connectedcomponenets(vertex);

        // add edges
        for (int x=0; x<edges;x++){
            int vertex1 = scanner.nextInt();
            int vertex2 = scanner.nextInt();

            graph.addEdge(vertex1, vertex2);
        }
        scanner.close();

        // call dfs
        graph.dfs();

        // print the connected componenets
        for(int x=0; x<graph.connectedComp.size();x++){
            System.out.println(graph.connectedComp.get(x));
        }
        
    }
}
