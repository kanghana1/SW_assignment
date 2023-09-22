# 백준 3단계

### **theme** - 반복문

풀이가 단순해서 별도의 정리를 하지 않은 문제 : 2, 3, 4, 5, 7, 8, 9

<hr>

### ✅ 문제 1 \_ 구구단

**문제**

N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

**필요개념**

for문을 이용했다.

**정답코드**

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        for (int i = 1 ; i <= 9 ; i++) {
            System.out.println(a + " * " + i + " = " + a * i);
        }
    }
}
```

---

### ✅ 문제 6 \_ 빠른 A+B 🌟

**문제**

본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

Java를 사용하고 있다면, `Scanner`와 `System.out.println` 대신 `BufferedReader`와 `BufferedWriter`를 사용할 수 있다. `BufferedWriter.flush`는 맨 마지막에 한 번만 하면 된다.

**필요개념**

Scanner와 System.out.println 대신 Buffer를 사용해보았다. Buffer를 사용하면 입력된 데이터가 바로 전달되지 않고 **버퍼를 거쳐 전달되어 데이터 처리 효율성이 올라간다**고 한다!

단, 값을 **줄바꿈 단위로 받기** 때문에, **StringTokenizer**를 이용해 가공작업을 거쳐야 한다. (공백 단위로 데이터를 받아야 하는 경우)

Buffer와 StringToken은 import로 가져와야 한다.

- Buffered들 불러오기

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
```

- StringTokenizer 불러오기

```java
import java.util.StringTokenizer;
```

- BufferedReader 사용시 주의사항 !!
  1. readLine() 메소드 이용시 **리턴값이 String으로 고정**된다!
     1. 그래서 해당 문제처럼 int로 가져오고 싶으면 형 변환을 해줘야 한다 (Integer.parseInt())
  2. 예외처리를 꼭 해아한다
     1. readLine() 쓸 때마다 try&catch문을 사용해도 된다.
     2. throws IOException을 사용하는게 편할 것이다.

**정답코드**

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int a = Integer.parseInt(br.readLine());

        for (int i = 0 ; i < a ; i++) {
            st = new StringTokenizer(br.readLine());
            bw.write((Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken())) + "\n");
        }
        bw.close(); // Writer 꼭 닫아주기!
    }
}
```

---

### ✅ 문제 10 \_ 별 찍기 - 2

**문제**

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

**필요개념**

이중 for문을 이용했다. for문 안의 첫 for문에는 공백을, 나머지 공간에 별을 찍으면 된다.

**정답코드**

이 코드보다 효율있는 코드 찾고싶다!

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = n ; i >= 1 ; i--) {
            for (int j = i - 1 ; j >= 1 ; j--) System.out.print(" ");
            for (int k = n - i; k >= 0 ; k--) System.out.print("*");
            System.out.println();
        }
    }
}
```

---

**3단계 문제 전체 풀이 완료** 

![3](../img/3.png)
