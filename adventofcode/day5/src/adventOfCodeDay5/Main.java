package adventOfCodeDay5; // Declare package name

import java.io.File; // Import file class
import java.io.FileNotFoundException; // Import FileNotFoundException class
import java.util.ArrayList; // Import ArrayList class
import java.util.List; // Import List class
import java.util.Scanner; // Import Scanner class

public class Main { // Declare public class Main

	public static void main(String[] args) throws FileNotFoundException { // Declare main method
		File inputFile = new File("day5Input.txt"); // Create File object for input file
		Scanner sc = new Scanner(inputFile); // Create Scanner object to read input file
		
		List<String> setupLines = new ArrayList<>(); // Create list to store setup lines
		
		String line = sc.nextLine(); // Read first line of input file
		
		while(line != "") { // Loop while line is not empty
			setupLines.add(line); // Add line to setupLines list
			if(sc.hasNext()) line = sc.nextLine(); // Read next line if available
			else break; // Break loop if no more lines
		}
		
		String[] numberLine = setupLines.get(setupLines.size()-1).strip().split("   "); // Split last line of setupLines list on "   "
		int numberOfCrates = Integer.valueOf(numberLine[numberLine.length-1]); // Get number of crates from last line
		
		setupLines.remove(setupLines.size()-1); // Remove last line from setupLines list
		
		List<CrateStack> crateStacks = new ArrayList<>(); // Create list of CrateStack objects
		// init stacks
		for(int i = 0; i<numberOfCrates; i++) crateStacks.add(new CrateStack()); // Create CrateStack objects and add to list
		
		// add all crates
		for(int i = setupLines.size()-1; i>=0; i--) { // Loop through setupLines list in reverse
			line = setupLines.get(i); // Get line
			// Skipping every fourth to get letters or nothing
			int p = 0; // Initialize counter
			for(int j = 1; j < line.length(); j += 4) { // Loop through line
				if(line.charAt(j) == ' ') { // Check for empty space
					p+=1; // Increment counter
					continue; // Skip iteration
				}
				Crate crate = new Crate(line.charAt(j)); // Create Crate object with current character
				crateStacks.get(p).addCrate(crate); // Add Crate object to corresponding CrateStack
				p+=1; // Increment counter
			}
		}
		
		while(sc.hasNext()) { // Loop while there are more lines to read
			line = sc.nextLine(); // Read line
			String[] words = line.split(" "); // Split line on spaces
			int nCrates = Integer.valueOf(words[1]); // Get number of crates to move from line
			CrateStack stackFrom = crateStacks.get(Integer.valueOf(words[3]) - 1); // Get CrateStack to move crates from 
			CrateStack stackTo = crateStacks.get(Integer.valueOf(words[5]) - 1); // Get CrateStack to move crates to
			List<Crate> crates = stackFrom.removeCrates(nCrates); // Remove crates from stackFrom
			stackTo.addCrates(crates); // Add crates to stackTo
		}
		
		// Write out top letter of each stack
		String letters = ""; // Initialize letters string
		for(CrateStack cs : crateStacks) { // Loop through crateStacks list
			letters += cs.topCrate(); // Add top letter of each stack to letters string
		}
		
		System.out.println(letters); // Print letters string
		
	}

}
