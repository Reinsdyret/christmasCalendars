package adventOfCodeDay5;

import java.util.List;

/**
 * Interface for Crate stack that will keep track of the stack
 * @author yral
 *
 */
public interface ICrateStack {
	
	/**
	 * Add a crate to the stack
	 * @param crate
	 */
	public void addCrate(Crate crate);
	
	public void addCrates(List<Crate> crates);
	
	public Crate removeCrate();
	
	public List<Crate> removeCrates(int n);
}
