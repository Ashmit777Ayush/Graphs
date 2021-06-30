import java.util.*;
public class SCC {
    // vertices
    int vertices;
    // adjacency list
    List<Integer> adjList[];
    // reverse graph
    List<Integer> adjListRev[];

    // vsited
    boolean visited[];

    // postOrder
    List<Integer> postVisit = new ArrayList<>();

    HashMap<Integer, List<Integer>> hashmap = new HashMap<>();
    //counter
    int counter=1;

    @SuppressWarnings("unchecked") SCC(int vertex){
        vertices = vertex;
        adjList = new ArrayList[vertex];
        adjListRev = new ArrayList[vertex];
        visited = new boolean[vertex];
        for (int x=0; x< vertex; x++){
            adjList[x]=new ArrayList<Integer>();
            adjListRev[x] = new ArrayList<Integer>();
        }
    }

    // add edge
    public void addEdge(int ver1, int ver2){
        adjList[ver1].add(ver2);
        adjListRev[ver2].add(ver1);
    }

    // post order
    public void post(int vertex){
        postVisit.add(vertex);
    }

    // explore Reverse
    public void exploreRev(int vertex){
        // first mark as true
        visited[vertex]=true;

        //
        Iterator<Integer> index = adjListRev[vertex].listIterator();
        while(index.hasNext()){
            int ver = index.next();
            // check
            if (visited[ver]==false){
                exploreRev(ver);
            }
        }
        // postvisit
        post(vertex);
    }


    // explore
    public void explore(int vertex){
        // mark as visiyted
        visited[vertex]=true;

        //add to the connexted component
        if (hashmap.containsKey(counter)==true){
            List<Integer> z = hashmap.get(counter);
            z.add(vertex);
            hashmap.put(counter, z);
        }
        else{
            List<Integer> z = new ArrayList<>();
            z.add(vertex);
            hashmap.put(counter, z);
        }

        Iterator<Integer> index = adjList[vertex].listIterator();
        while(index.hasNext()){
            int ver = index.next();
            if (visited[ver]==false){
                explore(ver);
            }
        }
    }


    // scc
    public void scc(){
        for (int vertex=0; vertex<vertices; vertex++){
            if (visited[vertex]==false){
                exploreRev(vertex);
            }
        }

        // make all visited fase
        for (int x=0;x<vertices;x++){
            visited[x]=false;
        }

        Collections.reverse(postVisit);

        for (int vertex :postVisit){
            if (visited[vertex]==false){
                explore(vertex);
                // increment the counter
                counter++;
            }
        }
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int vertex = scanner.nextInt();
        int edge = scanner.nextInt();

        // amke object
        SCC graph = new SCC(vertex);

        for(int x=0; x<edge; x++){
            int ver1 = scanner.nextInt();
            int ver2 = scanner.nextInt();
            graph.addEdge(ver1, ver2);
        }
        scanner.close();
        graph.scc();

        for (int x=1; x<graph.hashmap.size()+1; x++){
            System.out.print(graph.hashmap.get(x));
        }

    }
}
