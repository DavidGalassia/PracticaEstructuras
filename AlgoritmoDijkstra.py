<html>
<head>
<title>AlgoritmoDijkstra.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #dca9dc;}
.s1 { color: #cdd3de;}
.s2 { color: #89ddff;}
.s3 { color: #66c7c7;}
.s4 { color: #4d6470; font-style: italic;}
.s5 { color: #9fa8bc;}
.s6 { color: #fb9551;}
</style>
</head>
<body bgcolor="#11242c">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
AlgoritmoDijkstra.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">heapq </span><span class="s0">import </span><span class="s1">heapify</span><span class="s2">, </span><span class="s1">heappop</span><span class="s2">, </span><span class="s1">heappush</span>

<span class="s0">class </span><span class="s1">Graph</span><span class="s3">:</span>
   <span class="s0">def </span><span class="s1">__init__</span><span class="s3">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">graph</span><span class="s3">: </span><span class="s1">dict </span><span class="s3">= {}):</span>
       <span class="s1">self</span><span class="s2">.</span><span class="s1">graph </span><span class="s3">= </span><span class="s1">graph  </span><span class="s4"># El diccionario del grafo es una lista de adyacencia</span>

   <span class="s0">def </span><span class="s1">add_edge</span><span class="s3">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">node1</span><span class="s2">, </span><span class="s1">node2</span><span class="s2">, </span><span class="s1">nodeWeight</span><span class="s3">):</span>
       <span class="s0">if </span><span class="s1">node1 </span><span class="s0">not in </span><span class="s1">self</span><span class="s2">.</span><span class="s1">graph</span><span class="s3">:  </span><span class="s4"># Revisa si el nodo ya existe dentro del grafo</span>
           <span class="s1">self</span><span class="s2">.</span><span class="s1">graph</span><span class="s3">[</span><span class="s1">node1</span><span class="s3">] = {}  </span><span class="s4"># Si no existe, crea ese nodo</span>
       <span class="s1">self</span><span class="s2">.</span><span class="s1">graph</span><span class="s3">[</span><span class="s1">node1</span><span class="s3">][</span><span class="s1">node2</span><span class="s3">] = </span><span class="s1">nodeWeight  </span><span class="s4"># Si el nodo ya existe, entonces crea la conexion de ese nodo1 con el nodo2</span>

   <span class="s0">def </span><span class="s1">shortest_distances</span><span class="s3">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">sourceNode</span><span class="s3">: </span><span class="s1">str</span><span class="s3">):</span>
       <span class="s1">distances </span><span class="s3">= {</span><span class="s1">node</span><span class="s3">: </span><span class="s1">float</span><span class="s3">(</span><span class="s5">&quot;inf&quot;</span><span class="s3">) </span><span class="s0">for </span><span class="s1">node </span><span class="s0">in </span><span class="s1">self</span><span class="s2">.</span><span class="s1">graph</span><span class="s3">}</span><span class="s4"># El peso inicial de todos los nodos es infinito</span>
       <span class="s1">distances</span><span class="s3">[</span><span class="s1">sourceNode</span><span class="s3">] = </span><span class="s6">0  </span><span class="s4"># El peso del nodo inicial es 0</span>

       <span class="s4"># Inicia una cola de prioridad</span>
       <span class="s1">priorityQueue </span><span class="s3">= [(</span><span class="s6">0</span><span class="s2">, </span><span class="s1">sourceNode</span><span class="s3">)]</span>
       <span class="s1">heapify</span><span class="s3">(</span><span class="s1">priorityQueue</span><span class="s3">)</span>

       <span class="s4"># Iniciamos una lista que no acepta elementos repetidos para guardar los nodos visitados</span>
       <span class="s1">visitedNodes </span><span class="s3">= </span><span class="s1">set</span><span class="s3">()</span>

       <span class="s0">while </span><span class="s1">priorityQueue</span><span class="s3">:  </span><span class="s4"># Mientras que la cola de prioridad no este vacia,</span>
           <span class="s1">currentDistance</span><span class="s2">, </span><span class="s1">currentNode </span><span class="s3">= </span><span class="s1">heappop</span><span class="s3">(</span><span class="s1">priorityQueue</span><span class="s3">) </span><span class="s4"># Obten el nodo con el peso minimo</span>

           <span class="s0">if </span><span class="s1">currentNode </span><span class="s0">in </span><span class="s1">visitedNodes</span><span class="s3">:</span>
               <span class="s0">continue  </span><span class="s4"># Si el nodo de menor peso ya lo visitamos, saltalo</span>
           <span class="s1">visitedNodes</span><span class="s2">.</span><span class="s1">add</span><span class="s3">(</span><span class="s1">currentNode</span><span class="s3">)  </span><span class="s4"># Si no lo hemos visitado, se añade a la lista de nodos visitados</span>

           <span class="s0">for </span><span class="s1">neighborNode</span><span class="s2">, </span><span class="s1">nodeWeight </span><span class="s0">in </span><span class="s1">self</span><span class="s2">.</span><span class="s1">graph</span><span class="s3">[</span><span class="s1">currentNode</span><span class="s3">]</span><span class="s2">.</span><span class="s1">items</span><span class="s3">():</span>
               <span class="s4"># Calcula la distancia desde el nodo actual a su vecino</span>
               <span class="s1">tentativeDistance </span><span class="s3">= </span><span class="s1">currentDistance </span><span class="s3">+ </span><span class="s1">nodeWeight</span>

               <span class="s0">if </span><span class="s1">tentativeDistance </span><span class="s3">&lt; </span><span class="s1">distances</span><span class="s3">[</span><span class="s1">neighborNode</span><span class="s3">]: </span><span class="s4">#Si la distancia teorica es menor a la distancia recorrida</span>
                   <span class="s1">distances</span><span class="s3">[</span><span class="s1">neighborNode</span><span class="s3">] = </span><span class="s1">tentativeDistance </span><span class="s4">#Se añade la distancia recorrida a ese nodo vecino</span>
                   <span class="s1">heappush</span><span class="s3">(</span><span class="s1">priorityQueue</span><span class="s2">, </span><span class="s3">(</span><span class="s1">tentativeDistance</span><span class="s2">, </span><span class="s1">neighborNode</span><span class="s3">)) </span><span class="s4">#Añade a la cola de prioridad ese nodo vecino</span>

       <span class="s1">nodePredecessors </span><span class="s3">= {</span><span class="s1">node</span><span class="s3">: </span><span class="s0">None for </span><span class="s1">node </span><span class="s0">in </span><span class="s1">self</span><span class="s2">.</span><span class="s1">graph</span><span class="s3">}</span>

       <span class="s0">for </span><span class="s1">node</span><span class="s2">, </span><span class="s1">distance </span><span class="s0">in </span><span class="s1">distances</span><span class="s2">.</span><span class="s1">items</span><span class="s3">():</span>
           <span class="s0">for </span><span class="s1">neighborNode</span><span class="s2">, </span><span class="s1">nodeWeight </span><span class="s0">in </span><span class="s1">self</span><span class="s2">.</span><span class="s1">graph</span><span class="s3">[</span><span class="s1">node</span><span class="s3">]</span><span class="s2">.</span><span class="s1">items</span><span class="s3">():</span>
               <span class="s0">if </span><span class="s1">distances</span><span class="s3">[</span><span class="s1">neighborNode</span><span class="s3">] == </span><span class="s1">distance </span><span class="s3">+ </span><span class="s1">nodeWeight</span><span class="s3">:</span>
                   <span class="s1">nodePredecessors</span><span class="s3">[</span><span class="s1">neighborNode</span><span class="s3">] = </span><span class="s1">node</span>

       <span class="s0">return </span><span class="s1">distances</span><span class="s2">, </span><span class="s1">nodePredecessors</span>

   <span class="s0">def </span><span class="s1">shortest_path</span><span class="s3">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">sourceNode</span><span class="s3">: </span><span class="s1">str</span><span class="s2">, </span><span class="s1">targetNode</span><span class="s3">: </span><span class="s1">str</span><span class="s3">):</span>
       <span class="s4"># Genera el diccionario de predecesores</span>
       <span class="s1">_</span><span class="s2">, </span><span class="s1">nodePredecessors </span><span class="s3">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">shortest_distances</span><span class="s3">(</span><span class="s1">sourceNode</span><span class="s3">)</span>

       <span class="s1">exploredPath </span><span class="s3">= []</span>
       <span class="s1">currentNode </span><span class="s3">= </span><span class="s1">targetNode</span>

       <span class="s4"># Se devuelve desde el nodo en el que este hacia el nodo origen</span>
       <span class="s0">while </span><span class="s1">currentNode</span><span class="s3">:</span>
           <span class="s1">exploredPath</span><span class="s2">.</span><span class="s1">append</span><span class="s3">(</span><span class="s1">currentNode</span><span class="s3">)</span>
           <span class="s1">currentNode </span><span class="s3">= </span><span class="s1">nodePredecessors</span><span class="s3">[</span><span class="s1">currentNode</span><span class="s3">]</span>

       <span class="s4"># Como estamos iniciando desde el ultimo nodo hasta el inicio, lo reversamos para mostrarlo:</span>
       <span class="s1">exploredPath</span><span class="s2">.</span><span class="s1">reverse</span><span class="s3">()</span>

       <span class="s0">return </span><span class="s1">exploredPath</span>


</pre>
</body>
</html>
