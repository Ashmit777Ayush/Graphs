import java.util.*;
public class Previsitpostvisit {
    // vertices in the graph
    private int vertices;
    // adjacent list
    private List<Integer> adjList[];
    // visited
    private boolean visited[];
    // pre
    private int pre[];
    // post
    private int post[];
    // cuunter
    private int counter=1;

    Previsitpostvisit(int v){
        vertices = v;
        adjList = new ArrayList[v];// assign length
        visited = new boolean[v];
        pre = new int[v];
        post = new int[v];

        for(int x=0; x<v; x++){
            adjList[x]=new ArrayList();
            visited[x] = false;
            pre[x]=-1;
            post[x]=-1;
        }
    }

    // add edges
    void addEdge(int vertex1, int vertex2){
        adjList[vertex1].add(vertex2);
        adjList[vertex2].add(vertex1);
    }

    // preorder assignment
    void preOrder(int vertex){
        pre[vertex]=counter;
        counter+=1;
    }

    // postOrder
    void postOrder(int vertex){
        post[vertex]=counter;
        counter+=1;
    }
    
    // explore
    void Explore(int vertex){
        // first mark as true of this index
        visited[vertex]=true;
        // assign for the preorder
        preOrder(vertex);

        // now iterate through the all neighbour of this vertex
        Iterator<Integer> i = adjList[vertex].listIterator();
        while(i.hasNext()){
            int ver = i.next();
            if (visited[ver]==false){
                Explore(ver);
            }
        }
        // for the postOrder
        postOrder(vertex);
    }

    //dfs
    void dfs(){
        for(int vertex=0; vertex<vertices; vertex++){
            if (visited[vertex]==false){
                Explore(vertex);
            }
        }
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int vertex = scanner.nextInt();
        int edge = scanner.nextInt();

        // make the object of the class
        Previsitpostvisit graph = new Previsitpostvisit(vertex);

        // make the adjacency list
        for (int x=0; x< edge; x++){
            int vertex1 = scanner.nextInt();
            int vertex2 = scanner.nextInt();

            graph.addEdge(vertex1, vertex2);
        }
        scanner.close();

        // do dfs
        graph.dfs();
        
        System.out.print("pre --> \t");
        for(int x=0; x<vertex;x++)System.out.print(graph.pre[x]+ " ");
        System.out.println();
        System.out.print("post --> \t");
        for(int x=0; x<vertex;x++)System.out.print(graph.post[x]+ " ");

    }
}
