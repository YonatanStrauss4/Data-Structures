//username1 - Strauss1
//id1      - 208582502
//name1    - Yonatan Strauss
//username2 - Taldotan
//id2      - 322712001
//name2    - Tal Dotan
/**
 * BinomialHeap
 *
 * An implementation of binomial heap over non-negative integers.
 * Based on exercise from previous semester.
 */
public class BinomialHeap
{
	public int size;
	public HeapNode last;
	public HeapNode min;
	public int numberOfTrees;


	public BinomialHeap(){  //O(1)
		this.size = 0;
		this.last = null;
		this.min = null;
		this.numberOfTrees = 0;
	}

	public HeapNode createHeapNode(int key, String info) {  //O(1)

		HeapItem item = new HeapItem(null,key, info);
		HeapNode node = new HeapNode(item);
		item.node = node;
		return node;

	}

	/**
	 *
	 * pre: key > 0
	 *
	 * Insert (key,info) into the heap and return the newly generated HeapItem.
	 *
	 */
	public HeapItem insert(int key, String info) //O(log(n))
	{
		this.numberOfTrees ++;   //updating number of trees (the linking will reduce what is needed)
		HeapNode newNode = createHeapNode(key, info);  //creating new node to insert
		HeapItem item = newNode.item;                  // creating an item to return

		//case 1 = inserting into empty heap
		if(this.last == null){
			this.last = newNode;
			this.min = newNode;
			this.size ++;   //updating tree size by one
			return item; //returning the node item
		}

		//case 2 = inserting to heap with 1 node
		if(this.size == 1){
			if(this.min.item.key > newNode.item.key){     //changing the min if needed
				this.min = newNode;
			}
			this.numberOfTrees--;     //reducing the number of trees after a special case link
			if(newNode.item.key < this.last.item.key){     //need to change places of nodes
				newNode.child = this.last;
				this.last.parent = newNode;
				this.min = newNode;
				this.last = newNode;
				newNode.rank ++;
			}
			else{  //no need to change places of nodes
				this.last.child = newNode;
				newNode.parent = this.last;
				this.last.rank ++;
			}
			this.size ++;   //updating tree size by one
			return item; //returning the node item
		}

		//case 3 = inserting to a heap with one tree (the tree has more than one node)
		if(this.last.next == this.last){
			if(this.min.item.key > newNode.item.key){     //changing the min if needed
				this.min = newNode;
			}
			this.last.next = newNode;
			newNode.next = this.last;
			this.size ++;   //updating tree size by one
			return item; //returning the node item
		}
		if(this.min.item.key > newNode.item.key){
			this.min = newNode;
		}

		//case 4 = if the heap first tree is from degree 1, doing the first link manually
		HeapNode firstNode = this.last.next;
		if (this.last.next.child == null){                      //special case (not so special more for comfort) of connecting the first node manually if it is a single node
			this.numberOfTrees--;                               //reducing the number of trees after a special case link
			if(this.last.next.item.key > newNode.item.key){
				HeapNode tmp2 = this.last.next.next;          //some pointers...
				newNode.child = this.last.next;
				this.last.next.parent = newNode;
				this.last.next.next = this.last.next;
				newNode.next = tmp2;
				this.last.next = newNode;
				newNode.rank ++;
			}
			else{
				this.last.next.child = newNode;     //some pointers...
				newNode.parent = this.last.next;
				this.last.next.rank ++;
				newNode = this.last.next;
			}
			firstNode = newNode.next;
		}
		//case 5 = regular inserting case, nothing special
		HeapNode tmp;
		while(newNode.rank == firstNode.rank && newNode != firstNode){    //connecting trees of same rank
			tmp = firstNode.next;
			newNode = linkinTrees(newNode, firstNode);
			if(this.last.parent != null){
				this.last = newNode;
			}
			newNode.next = tmp;                        //some pointers...
			this.last.next = newNode;
			firstNode = tmp;

		}
		if(this.last.next !=last) {
			newNode.next = firstNode;                 //some pointers...
			this.last.next = newNode;
		}
		this.size ++;   //updating tree size by one
		if(this.min.item.key > newNode.item.key){     //changing the min if needed
			this.min = newNode;
		}
		return item; //returning the node item
	}

	/**
	 *
	 * Delete the minimal item
	 *
	 */
	public void deleteMin() { // O(log(n))
		HeapNode node = this.min;
		// in this first part of the code, we want to update the min and last pointers of this bin heap, according to the current min and its structure
		if (this.last.next == this.last) {	// if the binomial heap contains only a single tree with min as its root
			this.last = null;
			this.min = null;
		} else if (this.min == this.last){		// if min is the root of the last tree in the heap
			HeapNode tempNode = last.next;
			this.min = tempNode;
			while (tempNode != this.last) {		// finding the new min node in the bin heap, and updating last node
				if (tempNode.item.key < this.min.item.key) {
					this.min = tempNode;
				}
				if (tempNode.next == this.last) {
					tempNode.next = last.next;
					this.last = tempNode;
					break;
				}
				tempNode = tempNode.next;
			}

		} else {							// if min is not the root of the last tree in the heap
			HeapNode tempNode = node.next;
			this.min = tempNode;
			while (tempNode != node) {		// finding the new min node in the bin heap
				if (tempNode.item.key < this.min.item.key) {
					this.min = tempNode;
				}
				if (tempNode.next == node) {
					tempNode.next = node.next;
					break;
				}
				tempNode = tempNode.next;
			}
		}


		// in this second part of the code, we want to create a new bin heap which contains min's children, and using meld, connect them to this bin heap
		if (node.child == null) {			// if min does not have any children (it's the root of a tree of size 1)
			this.numberOfTrees--;
			this.size--;
			return;
		}
		// in this case node has at least one child:
		BinomialHeap newBin = new BinomialHeap(); 		// creating a new bin heap which contains min's children
		newBin.last = node.child;
		newBin.min = node.child;
		newBin.numberOfTrees = 1;
		HeapNode temp = node.child;
		int tempSize = (int) Math.pow(2, node.child.rank);
		newBin.size = tempSize;
		temp.parent = null;
		temp = temp.next;
		while (temp != node.child) {		// finding the min of newBin heap, and updating its size
			if (temp.item.key < newBin.min.item.key) {
				newBin.min = temp;
			}
			temp.parent = null;
			tempSize = (int) Math.pow(2, temp.rank);
			newBin.size += tempSize;
			newBin.numberOfTrees++;
			temp = temp.next;
		}
		this.numberOfTrees--;
		this.size = this.size - newBin.size - 1;		// updating the size of this bin heap
		this.meld(newBin);	// using meld to connect this bin heap with newBin heap
	}

	/**
	 *
	 * Return the minimal HeapItem
	 *
	 */
	public HeapItem findMin() { // O(1)
		if (this.empty()) {		// if this Binomial Heap is empty
			return null;
		}
		return this.min.item;
	}

	/*
	 * swapping between the items of two nodes (used for decrease key)
	 */
	public void swapItems(HeapNode node1, HeapNode node2) {	// O(1)
		HeapItem item1 = node1.item;
		HeapItem item2 = node2.item;
		node1.item = item2;
		item2.node = node1;
		node2.item = item1;
		item1.node = node2;
	}

	/**
	 *
	 * pre: 0<diff<item.key
	 *
	 * Decrease the key of item by diff and fix the heap.
	 *
	 */
	public void decreaseKey(HeapItem item, int diff) { // O(log(n))
		item.key = item.key - diff;		// decreasing the key as requested
		HeapNode node = item.node;
		while (node.parent != null) {		// sifting up the tree and switching between items if needed
			if (node.item.key < node.parent.item.key) {
				swapItems(node, node.parent);
				node = node.parent;
			} else {		// if we reached a node whose key is larger than its parent's key we can stop
				break;
			}
		}
		if (item.key < this.min.item.key) {		// updating this.min if needed
			this.min = item.node;
		}
	}

	/**
	 *
	 * Delete the item from the heap.
	 *
	 */
	public void delete(HeapItem item) {	// O(log(n))
		if (item.node == this.min) {		// if the node we want to delete is actually this.min then we can call deleteMin()
			this.deleteMin();
			return;
		}
		int x = (int)Double.NEGATIVE_INFINITY;		// decreasing the key of the node we want to delete, making it the min node in this bin heap, and calling deleteMin()
		this.decreaseKey(item, x);
		this.deleteMin();
	}

	/**
	 *
	 * Meld the heap with heap2
	 *
	 */
	public void meld(BinomialHeap heap2) {  //O(log(n))
		int lnHeap1 = Integer.toBinaryString(this.size).length();    //getting the number of roots of each heap
		int lnHeap2 = Integer.toBinaryString(heap2.size).length();
		if(Integer.toBinaryString(this.size).equals("0")){
			lnHeap1 = 0;
		}
		if(Integer.toBinaryString(heap2.size).equals("0")){
			lnHeap2 = 0;
		}
		if(lnHeap1 == 0){  //this heap is empty, if heap 2 or both empty, there is nothing to do
			this.last = heap2.last;   //switching between the heaps
			this.min = heap2.min;
			this.size = heap2.size;
			this.numberOfTrees = heap2.numberOfTrees;
			heap2.last = null;         //making the second heap unusable
			heap2.min = null;
			heap2.size = 0;
			heap2.numberOfTrees = 0;
		}
		if (lnHeap1 != 0 && lnHeap2 != 0) {   //both heaps have nodes
			if (heap2.size == 1) {                                          //if heap2 has one node perform insertion
				this.insert(heap2.last.item.key, heap2.last.item.info);
			}
			else {
				if(this.size == 1){
					heap2.insert(this.last.item.key, this.last.item.info);
					this.last = heap2.last;   //switching between the heaps
					this.min = heap2.min;
					this.size = heap2.size;
					this.numberOfTrees = heap2.numberOfTrees;
					heap2.last = null;         //making the second heap unusable
					heap2.min = null;
					heap2.size = 0;
					heap2.numberOfTrees = 0;
				}

			else{
					int carry = 0;
					if (this.min.item.key > heap2.min.item.key) {        //updating the minimum of this if needed
						this.min = heap2.min;
					}
					HeapNode heap1First = this.last.next;    //getting the root of smallest tree in heaps
					HeapNode heap2First = heap2.last.next;
					StringBuilder binRepHeap1 =  new StringBuilder(Integer.toBinaryString(this.size));       //getting the binary representation of the heaps to a string
					binRepHeap1.reverse();
					StringBuilder binRepHeap2 =  new StringBuilder(Integer.toBinaryString(heap2.size));
					binRepHeap2.reverse();
					char[] charsOfBinRepHeap1 = new char[binRepHeap1.length()];         //getting the binary representation of the heaps to an array
					binRepHeap1.getChars(0, binRepHeap1.length(), charsOfBinRepHeap1, 0);
					char[] charsOfBinRepHeap2 = new char[binRepHeap2.length()];
					binRepHeap2.getChars(0, binRepHeap2.length(), charsOfBinRepHeap2, 0);
					int i = 0; //for inserting the roots to the array
					int largest = Math.max(lnHeap1, lnHeap2); //number of trees in the heap with more trees
					HeapNode[] arrHeap1 = new HeapNode[largest];         //initializing arrays for roots of trees
					HeapNode[] arrHeap2 = new HeapNode[largest];
					HeapNode[] arrFinalHeap = new HeapNode[largest + 1];

					for (char ch : charsOfBinRepHeap1) {        //inserting roots to array of this
						if (Character.compare(ch, '1') == 0) {  //inserting a root
							arrHeap1[i] = heap1First;
							heap1First = heap1First.next;
						} else {                                  //inserting null
							arrHeap1[i] = null;
						}
						i++;
					}
					i = 0; //reset i
					for (char ch : charsOfBinRepHeap2) {        //inserting roots to array of heap 2
						if (Character.compare(ch, '1') == 0) {  //inserting a root
							arrHeap2[i] = heap2First;
							heap2First = heap2First.next;
						} else {                                  //inserting null
							arrHeap2[i] = null;
						}
						i++;
					}
					HeapNode carryTmp = null;
					for (int j = 0; j < largest; j++) {                     //loop that makes the linking between the tree like a binary addition, with all the cases
						if (carry == 0) {                                   //some cases of binary addition. arrFinalHeap will have the melded heap at the end
							if (arrHeap1[j] != null && arrHeap2[j] != null) {
								carryTmp = linkinTrees(arrHeap1[j], arrHeap2[j]);
								carry = 1;
								continue;
							}
							if (arrHeap1[j] == null && arrHeap2[j] == null) {
								arrFinalHeap[j] = null;
								continue;
							}
							if (arrHeap1[j] == null) {
								arrFinalHeap[j] = arrHeap2[j];
								continue;
							}
							if (arrHeap2[j] == null) {
								arrFinalHeap[j] = arrHeap1[j];
								continue;
							}
						} else {
							if (arrHeap1[j] != null && arrHeap2[j] != null) {
								arrFinalHeap[j] = carryTmp;
								carryTmp = linkinTrees(arrHeap1[j], arrHeap2[j]);
								continue;
							}
							if (arrHeap1[j] == null && arrHeap2[j] == null) {
								arrFinalHeap[j] = carryTmp;
								carryTmp = null;
								carry = 0;
								continue;
							}
							if (arrHeap1[j] == null) {
								arrFinalHeap[j] = null;
								carryTmp = linkinTrees(carryTmp, arrHeap2[j]);
								continue;
							}
							if (arrHeap2[j] == null) {
								arrFinalHeap[j] = null;
								carryTmp = linkinTrees(carryTmp, arrHeap1[j]);
								continue;
							}
						}
					}
					if(carryTmp != null){                      //adding the carry Node if needed
						arrFinalHeap[largest] = carryTmp;
					}

					if(this.min.parent != null){
						this.min = this.min.parent;
					}
					//now we make the connections between the roots of the final heap
					//first remove the nulls from the final array
					int notNull = 0;
					for (int n = 0; n < arrFinalHeap.length; n++) {      //counting the nulls
						if (arrFinalHeap[n] != null)
							notNull++;
					}

					HeapNode[] cleanFinalArr = new HeapNode[notNull];
					this.numberOfTrees = cleanFinalArr.length;        //updating the number of trees
					int index = 0;
					for (HeapNode node : arrFinalHeap) {              //cleaning the final array by removing the nulls
						if (node != null) {
							cleanFinalArr[index] = node;
							index++;
						}
					}

					//making the connections between the roots to get the melded heap
					if (cleanFinalArr.length == 1) {                //special case if the heap has one tree
						cleanFinalArr[0].next = cleanFinalArr[0];
						this.last = cleanFinalArr[0];
					}
					else {
						int finalIndex = 0;                         //making the connections
						for (int m = 0; m < cleanFinalArr.length; m++) {
							if (m + 1 < cleanFinalArr.length) {
								cleanFinalArr[m].next = cleanFinalArr[m + 1];
							}
							if (m + 1 == cleanFinalArr.length) {
								finalIndex = m;
							}
						}
						cleanFinalArr[finalIndex].next = cleanFinalArr[0];
						this.last = cleanFinalArr[finalIndex];
					}
				}
				this.size = this.size + heap2.size;  //updating the size
				heap2.last = null;         //making the second heap unusable
				heap2.min = null;
				heap2.size = 0;
				heap2.numberOfTrees = 0;
			}
		}

	}



	public HeapNode linkinTrees(HeapNode firstTree, HeapNode secondTree){   //O(1)
		this.numberOfTrees --;  //reducing the number of trees because of a link
		HeapNode larger;
		HeapNode smaller;
		if(firstTree.item.key > secondTree.item.key){      //deciding which node needs to be on top
			larger = firstTree;
			smaller = secondTree;
		}
		else{
			larger = secondTree;
			smaller = firstTree;
		}
		if(firstTree.child == null && secondTree.child == null){
			smaller.child = larger;
			larger.parent = smaller;
			larger.next = larger;
			smaller.rank++;
			if(this.min.parent != null){
				this.min = this.min.parent;
			}
			return smaller;
		}
		else {
			larger.next = smaller.child.next;     //making the necessary connections
			smaller.child.next = larger;
			smaller.child = larger;
			larger.parent = smaller;
			smaller.rank++;
			if(this.min.parent != null){
				this.min = this.min.parent;
			}
			return smaller;
		}
	}




	/**
	 *
	 * Return the number of elements in the heap
	 *
	 */
	public int size()   //O(1)
	{
		return this.size;
	}

	/**
	 *
	 * The method returns true if and only if the heap
	 * is empty.
	 *
	 */
	public boolean empty()  //O(1)
	{
		return (this.last == null);
	}

	/**
	 *
	 * Return the number of trees in the heap.
	 *
	 */
	public int numTrees() //O(1)
	{
		return this.numberOfTrees;
	}


	/**
	 * Class implementing a node in a Binomial Heap.
	 *
	 */
	public class HeapNode{
		public HeapItem item;
		public HeapNode child;
		public HeapNode next;
		public HeapNode parent;
		public int rank;

		public HeapNode(HeapItem item){  //O(1)

			this.item = item;
			this.child = null;
			this.next = this;
			this.parent = null;
			this.rank = 0;
		}
	}

	/**
	 * Class implementing an item in a Binomial Heap.
	 *
	 */
	public class HeapItem{
		public HeapNode node;
		public int key;
		public String info;

		public HeapItem(HeapNode node, int key, String info) {  //O(1)
			this.node = node;
			this.key = key;
			this.info = info;
		}
	}
	}


