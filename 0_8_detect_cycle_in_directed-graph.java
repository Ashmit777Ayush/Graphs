import java.util.*;
public class FindCycle {
    // number of vertices
    private int vertices;
    // adjacency list
    private List<Integer> adjList[];
    // for visit
    private boolean visit[];
    // array for checking 
    private boolean check[];
    // cycle
    private boolean cycle=false;

    FindCycle(int vertex){
        vertices = vertex;
        // adjacency list 
        adjList = new ArrayList[vertex];
        // check 
        check = new boolean[vertex];
        // visit
        visit = new boolean[vertex];

        for (int x=0; x<vertex; x++){
            //  assigning new list to the at each index
            adjList[x] = new ArrayList();

            visit[x]=false;
            check[x]=false;
        }
    }

    // add Edge
    void addEdge(int vertex1, int vertex2){
        adjList[vertex1].add(vertex2);
    }

    // explore
    void Explore(int vertex){
        // first mark as the visited
        visit[vertex]=true;

        // make in the check as true 
        check[vertex]=true;

        // now iterate through it's neighbour
        Iterator<Integer> i = adjList[vertex].listIterator();

        while(i.hasNext()){
            int ver = i.next();
            if (visit[ver]==false){
                Explore(ver);
            }
            else if(check[ver]==true){
                cycle=true;
                return;
            }
            else{
                ;
            }
        }
    }

    // dfs
    void dfs(){
        //  go through all the edges
        for (int vertex=0; vertex<vertices; vertex++){
            //  if not visited then explotre the vertex
            if (visit[vertex]==false){
                Explore(vertex);
            }
        }
    }
    
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int vertex = scanner.nextInt();
        int edge = scanner.nextInt();

        FindCycle graph=new FindCycle(vertex);
        //  add the edges
        for(int x=0; x<edge; x++){
            int vertex1 = scanner.nextInt();
            int vertex2 = scanner.nextInt();

            //  add edge
            graph.addEdge(vertex1, vertex2);
        }

        graph.dfs();

        if (graph.cycle==true) System.out.println("Graph is having the cycle");
        else System.out.println("Graph do not contains the cycle");

    }
}
