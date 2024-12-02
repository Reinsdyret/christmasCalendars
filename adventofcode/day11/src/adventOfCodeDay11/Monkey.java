package adventOfCodeDay11;

import java.math.BigInteger;
import java.util.Collection;
import java.util.LinkedList;
import java.util.Queue;

/**
 * monkey
 */
public class Monkey {

 Queue<BigInteger> items;
 BigInteger inspectedCount = new BigInteger("0");

 Monkey(Collection<BigInteger> items){
   this.items = new LinkedList<BigInteger>(items);
 }

 public void addItem(BigInteger item){
  this.items.add(item);
  }

 public BigInteger getItem(){
   return this.items.poll();
 }

 public Boolean hasItems(){
   return !items.isEmpty();
 }

 public BigInteger getInspectedCount(){
   return this.inspectedCount;
 }

 public void addInspectedCount(BigInteger i){
   this.inspectedCount.add(i);
 }
 
 public String toString() {
	 return "Monkey has inspected " + this.getInspectedCount() + "\n and is holding " + this.items.toString();
 }
}
