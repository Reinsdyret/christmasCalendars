package adventOfCodeDay7;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	// Stack to keep track of directories cd'd into
	static Stack<Directory> dirStack = new Stack<>();
	
	// SumSize
	static int size = 0;

	public static void main(String[] args) {
		dirStack.add(new Directory("root",0));
		
		File inputFile = new File("day7TestInput.txt");
		Scanner sc;
		try {
			sc = new Scanner(inputFile);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return;
		}
		
		
		// Skip first line
		sc.nextLine();
		
		while(sc.hasNext()) {
			String line = sc.nextLine();
			String[] words = line.split(" ");
			if(words[1].equals("cd")) {
				handleCD(words[2], sc);
			}
		}
		
		System.out.println(size);
	}
	
	private static void handleCD(String dir, Scanner sc) {
		System.out.println(dirStack.toString());
		if(dir.equals("..")) {
			Directory popped = dirStack.pop();
			if(popped.getSize() <= 100000) size += popped.getSize();
			return;
		}
		
		dirStack.add(new Directory(dir,0));
		String line = sc.nextLine();
		while((sc.hasNext())) {
			System.out.println(line);
			String[] words = line.split(" ");
			
			if(words[0].equals("$")) {
				return;
			}
			
			// Skip dirs cause we wanna add sizes
			if(words[0].equals("dir")) {
				line = sc.nextLine();
				System.out.println(line);
				continue;
			}
			
			// Add size to all parent dirs
			addSize(Integer.valueOf(words[0]));
			
			line = sc.nextLine();
		}
	}
	
	private static void addSize(int size) {
		for(Directory dir : dirStack) {
			//System.out.println("helo");
			dir.addSize(size);
			//System.out.println(dir.toString());
		}
	}

}
