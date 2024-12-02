package adventOfCodeDay7;

public class Directory {
	private String name;
	private int size;
	
	public Directory(String name, int size) {
		super();
		this.name = name;
		this.size = size;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getSize() {
		return size;
	}

	public void setSize(int size) {
		this.size = size;
	}
	
	public void addSize(int size) {
		this.size += size;
	}
	
	public String toString() {
		return name + " : " + size;
	}

}
