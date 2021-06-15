import java.util.*;
public class TopologicalSort {
    // number of vertices
    private int vertices;
    //  adjacency list
    private List<Integer> adjList[];
    // visit 
    private boolean visit[];
    // post
    private List<Integer> post = new ArrayList<>();

    @SuppressWarnings("unchecked") TopologicalSort(int vertex){
        vertices = vertex;
        adjList = new ArrayList[vertex];
        visit = new boolean[vertex];
        for (int x=0; x< vertex; x++){
            adjList[x] = new ArrayList<Integer>();
            visit[x] = false;
        }
    }

    //  add edge
    void addEdge(int vertex1, int vertex2){
        adjList[vertex1].add(vertex2);
    }

    // postVisit
    void postVisit(int vertex){
        post.add(vertex);
    }

    // explore
    void Explore(int vertex){
        //  mark as bvisited
        visit[vertex]=true;

        //iterate
        Iterator<Integer> i = adjList[vertex].listIterator();
        while(i.hasNext()){
            int ver = i.next();
            if (visit[ver]==false){
                Explore(ver);
            }
        }
        postVisit(vertex);
    }

    //dfs
    void dfs(){
        for (int vertex=0; vertex<vertices; vertex++){
            if (visit[vertex]==false){
                Explore(vertex);
            }
        }
    }


    public static void main(String[] args){
        Scanner scanner =new Scanner(System.in);

        int vertex = scanner.nextInt();
        int edge = scanner.nextInt();

        TopologicalSort graph = new TopologicalSort(vertex);

        for (int x=0; x<edge; x++){
            int vertex1 = scanner.nextInt();
            int vertex2 = scanner.nextInt();

            //  add to the adjacent list
            graph.addEdge(vertex1, vertex2);
        }
        scanner.close();

        graph.dfs();
        
        Collections.reverse(graph.post);
        System.out.print(graph.post);
    }
}
