import sys
import subprocess

def main(args):

    cannot_contain = ["public Book(",
                      "public String getTitle() ",
                      "public void setTitle(",
                      "public String getAuthor()",
                      "public void setAuthor(",
                      "public double getPrice()",
                      "public void setPrice(",
                      "public String toString()",
                      "public boolean equals(",
                      "public int hashCode()"]
    data = "@Data"

    total_points = 10
    code_compiles = True
    
    result = subprocess.run(['javac', '-proc:full', '-cp', '.;./lib/lombok.jar', 'Book.java'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if result.stderr != "":
        print(result.stderr)
        code_compiles = False
        total_points = 0
    else:
        
        result = subprocess.run(["type", "Book.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        for code_snippet in cannot_contain:
            if code_snippet in result.stdout:
                print("Deducting 1 point for %s not being replaced by Lombok annotation" % code_snippet)
                total_points -= 1

        if data in result.stdout:
            total_points -= 2

        result = subprocess.run(['javac', '-proc:full', '-cp', '.;./lib/lombok.jar', 'Main.java'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.stderr != "":
            print(result.stderr)
            code_compiles = False
            total_points -= 2

        if code_compiles:
            result = subprocess.run(['java', '-cp', '.;./lib/lombok.jar', 'Main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

            correct_answer = "Book(title=Effective Java, author=Joshua Bloch, price=45.99)\nfalse\n"

            assert(result.stdout == correct_answer)
        else:
            print("The Main.java class did not compile correctly with the given Book.java class")

    print("Score: %d / 10" % total_points)

if __name__ == '__main__':
    main(sys.argv[1:])
