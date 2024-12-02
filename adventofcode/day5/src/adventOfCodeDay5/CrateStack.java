package adventOfCodeDay5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class CrateStack implements ICrateStack {
	
	private Stack<Crate> stack;
	
	CrateStack(){
		stack = new Stack<Crate>();
	}
	
	CrateStack(List<Crate> crates){
		stack = new Stack<Crate>();
		for(Crate c : crates) {
			stack.push(c);
		}
	}
	
	@Override
	public void addCrate(Crate crate) {
		stack.push(crate);
	}

	@Override
	public void addCrates(List<Crate> crates) {
		for(Crate c : crates) {
			addCrate(c);
		}
	}

	@Override
	public Crate removeCrate() {
		if (stack.isEmpty()) return null;
		
		return stack.pop();
	}

	@Override
	public List<Crate> removeCrates(int n) {
		if (n > stack.size()) return null;
		
		List<Crate> crates = new ArrayList<>();
		for(int i = 0; i<n; i++) {
			crates.add(stack.pop());
		}
		// Fixing the updated terms of part 2
		//Collections.reverse(crates);
		return crates;
	} 
	
	public Crate topCrate() {
		return stack.peek();
	}
	
	public String toString() {
		return stack.toString();
	}

}
