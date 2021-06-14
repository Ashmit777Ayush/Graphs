import java.util.*;
public class DFS {
    // attributes for this class
    // vertices
    private int v;
    // adjacency list
    private List<Integer> adjList[];
    // visited  to check a vertex is visited or not in Explore method
    private boolean visited[];
    // for the preOrder traversal
    private int pre[];
    // counter for the preorder traversal
    private int counterPre = 0;

    // for assigning all the pre defined data structure
    DFS(int ver){
        // assign the nu,mber of vertex
        v = ver;
        // assign the number of boolean at it's vertex
        visited = new boolean[ver];
        // assisgn the array with the vertex length
        pre = new int[ver];
        // asssigning the adjList length
        adjList = new ArrayList[ver];

        // now going throgh the loop and adding the newList to adjList each index , in pre making all -1, and false in all visited
        for (int x=0; x<ver; x+=1){
            adjList[x] = new ArrayList();

            // for the visited boolean value false
            visited[x] = false;

            // pre 
            pre[x]=-1;
        }
    }

    // method to add the edge
    // as it is undirected we have to add n both direction
    void addEdge(int vertex1, int vertex2){
        adjList[vertex1].add(vertex2);
        adjList[vertex2].add(vertex1);
    }
    
    // for exploring the vertex
    void Explore(int vertex){
        // first mark it as true as it has been visited
        visited[vertex]=true;

        //now make the pre at the counterPre index this vertex
        pre[counterPre] = vertex;
        // also increase the counterPre for next iteration
        counterPre+=1;

        // do exploration
        // using Iterator to iterate the adjList
        Iterator<Integer> i = adjList[vertex].listIterator();
        while(i.hasNext()){
            int ver = i.next();

            // check is it visited or not if not then again explore that ver
            if (visited[ver]==false){
                Explore(ver);
            }
        }
    }

    // dfs depth forst search
    void dfs(){
        // start from the index 0
        for (int vertex=0; vertex<v; vertex++){
            // check visited or not
            if (visited[vertex]==false){
                Explore(vertex);
            }
        }
    }
    public static void main(String[] args){
        //  for scanning
        Scanner scanner = new Scanner(System.in);

        int ver = scanner.nextInt();// having the vertex number
        int edge = scanner.nextInt();// having the edge number

        DFS graph = new DFS(ver);// defing the graph 

        // now make the edges as adjacency List
        for (int x=0; x< edge; x++){
            int vertex1= scanner.nextInt();
            int vertex2= scanner.nextInt();

            // add the edge
            graph.addEdge(vertex1, vertex2);
        }
        scanner.close();
        
        // now do depth first search
        graph.dfs();

        for(int x=0; x<ver;x++) System.out.print(graph.pre[x]+"\t");
    }
}
