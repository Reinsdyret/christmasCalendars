package adventOfCodeDay11;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * Main
 */
public class Main {
    public static int[] inspectedCount = new int[8];
 public static void main(String[] args) {
    List<Monkey> monkeyList = setup();
    int rounds = 10000;
    for (int index = 0; index < inspectedCount.length; index++) {
      inspectedCount[index] = 0;
    }
    List<Function<BigInteger, BigInteger>> operations = Arrays.asList(
      num -> num.multiply(BigInteger.valueOf(3)),
      num -> num.add(BigInteger.valueOf(7)),
      num -> num.add(BigInteger.valueOf(5)),
      num -> num.add(BigInteger.valueOf(8)),
      num -> num.add(BigInteger.valueOf(4)),
      num -> num.multiply(BigInteger.valueOf(2)),
      num -> num.add(BigInteger.valueOf(6)),
      num -> num.multiply(num)
    );

    List<Function<BigInteger,Integer>> throwToOperations = Arrays.asList(
      num -> divBy(num, 5) ? 2 : 7,
      num -> divBy(num, 2) ? 3 : 6,
      num -> divBy(num, 13)? 5 : 4,
      num -> divBy(num, 19)? 6 : 0,
      num -> divBy(num, 11)? 3 : 1,
      num -> divBy(num, 3) ? 4 : 1,
      num -> divBy(num, 7) ? 7 : 0,
      num -> divBy(num, 17)? 2 : 5
    );
 
    for (int i= 0;  i< rounds; i++) {
      System.out.println(i);
      for(int monkey = 0; monkey < monkeyList.size(); monkey++){
        monkeyAction(monkeyList, monkey, operations, throwToOperations);
      }
    }
    System.out.println(monkeyList.toString());
    Arrays.sort(inspectedCount);
    inspectedCount = reverse(inspectedCount, 8); 
    System.out.println(inspectedCount.toString());
    System.out.println(inspectedCount[0] * inspectedCount[1]);

  }

 static int[] reverse(int a[], int n) {
   int[] b = new int[n];
   int j = n;
   for (int i = 0; i < n; i++) {
     b[j - 1] = a[i];
     j = j - 1;
   }
   // printing the reversed array
   System.out.println("Reversed array is: \n");
   for (int k = 0; k < n; k++) {
     System.out.println(b[k]);
   }
   return b;
 }

  private static List<Monkey> setup(){
    List<Monkey> monkeyList = new ArrayList<>();
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(78,53,89,51,52,59,58,85))));
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(64))));
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(71, 93, 65, 82))));
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(67, 73, 95, 75, 56, 74))));
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(85, 91, 90))));
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(67, 96, 69, 55, 70, 83, 62))));
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(53, 86, 98, 70, 64))));
    monkeyList.add(new Monkey(integerListToBigIntegerList(Arrays.asList(88, 64))));
    return monkeyList;
  }
  
  private static List<BigInteger> integerListToBigIntegerList(List<Integer> list){
	  List<BigInteger> coverList = list.stream()
		        .map(i -> BigInteger.valueOf(i))
		        .collect(Collectors.toList());
	  return coverList;
  }

  private static void monkeyAction(List<Monkey> monkeyList, int monkey, List<Function<BigInteger,BigInteger>> operations, List<Function<BigInteger,Integer>> throwToOperations){
      Monkey monkeyCurr = monkeyList.get(monkey);
      while(monkeyCurr.hasItems()){
        BigInteger item = monkeyCurr.getItem();
        item = operations.get(monkey).apply (item);
        item = item.mod(BigInteger.valueOf(9699690));
        //item /= 3;
        Integer throwTo = throwToOperations.get(monkey).apply(item);
        monkeyList.get(throwTo).addItem(item);
        inspectedCount[monkey] += 1;
      }
  }

  private static Boolean divBy(BigInteger num, int mod){
    return num.mod(BigInteger.valueOf(mod)).equals(BigInteger.valueOf(0));
  }
}
