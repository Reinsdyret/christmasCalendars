package adventOfCodeDay5;

public class Crate {
	private Character letter;
	
	Crate(Character letter){
		this.letter = letter;
	}
	
	public Character getLetter() {
		return this.letter;
	}
	
	public String toString() {
		return getLetter().toString();
	}
}
