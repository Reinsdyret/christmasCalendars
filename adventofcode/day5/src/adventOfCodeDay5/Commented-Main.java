
/**
 * CrateStack class
 */
class CrateStack {
	
	private List<Crate> crates; // Create list of Crate objects
	
	/**
	 * CrateStack constructor
	 */
	public CrateStack() {
		this.crates = new ArrayList<>(); // Initialize crates list
	}
	
	/**
	 * Add Crate object to CrateStack
	 * @param crate Crate object to add
	 */
	public void addCrate(Crate crate) {
		this.crates.add(crate); // Add Crate object to crates list
	}
	
	/**
	 * Add list of Crate objects to CrateStack
	 * @param crates List of Crate objects to add
	 */
	public void addCrates(List<Crate> crates) {
		this.crates.addAll(crates); // Add all Crate objects to crates list
	}
	
	/**
	 * Remove specified number of Crate objects from CrateStack
	 * @param n Number of Crate objects to remove
	 * @return List of Crate objects removed
	 */
	public List<Crate> removeCrates(int n) {
		List<Crate> removedCrates = new ArrayList<>(); // Create list to store removed crates
		for(int i = 0; i<n; i++) { // Loop n times
			removedCrates.add(this.crates.remove(this.crates.size()-1)); // Add last Crate object from crates list to removedCrates list and remove from crates list
		}
		return removedCrates; // Return removedCrates list
	}
	
	/**
	 * Get top Crate object from CrateStack
	 * @return Top Crate object
	 */
	public char topCrate() {
		return this.crates.get(this.crates.size()-1).getLetter(); // Return letter of last Crate object in crates list
	}

}

/**
 * Crate class
 */
class Crate {
	
	private char letter; // Declare letter field
	
	/**
	 * Crate constructor
	 * @param letter Letter of Crate object
	 */
	public Crate(char letter) {
		this.letter = letter; // Set letter field
	}
	
	/**
	 * Get letter of Crate object
	 * @return Letter of Crate object
	 */
	public char getLetter() {
		return this.letter; // Return letter field
	}

}