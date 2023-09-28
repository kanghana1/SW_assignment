# 백준 7단계

### **theme** - 이차원 배열

<br>

### ✅ 문제 1 \_ 행렬덧셈

**문제**

N\*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오

첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

**필요개념**

우선 A와 B 배열의 크기는 같다는 점을 이용하여 A 배열의 원소 먼저 스캐너를 이용해 받아주었다. 이후 새 이중반복문을 만들어서 입력받음과 동시에 A배열에 더해가는 작업을 했다.

이렇게 하면 배열을 한 개만 선언해도 된다고 생각했다.

특별한 메소드는 사용하지 않았다.

**정답코드**

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();

        int[][] arr = new int[x][y];

        for (int i = 0 ; i < arr.length; i++) {
            for (int j = 0 ; j < arr[i].length ; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        for (int i = 0 ; i < arr.length; i++) {
            for (int j = 0 ; j < arr[i].length ; j++) {
                System.out.print((arr[i][j] += sc.nextInt()) + " ");
            }
            System.out.println();
        }
    }
}
```

---

### ✅ 문제 2 \_ 최댓값

**문제**

9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

**필요개념**

이 문제도 입력과 동시에 이전까지의 max값과 비교하고, max값의 index를 받아놓으면서 풀이를 진행했다.

변수의 **초기값을 선언해**주어야 한다는 점 잊지 말기!

**정답코드**

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int a;
        int max = -1;
        int maxX = -1;
        int maxY = -1;

        for (int i = 1 ; i <= 9 ; i++) {
            for (int j = 1 ; j <= 9 ; j++) {
                a = sc.nextInt();
                if (max < a) {
                    max = a;
                    maxX = i;
                    maxY = j;
                }
            }
        }
        System.out.println(max);
        System.out.print(maxX + " " + maxY);

    }
}
```

---

### ✅ 문제 3 \_ 세로읽기

**문제**

아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.

이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다. 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다.

한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다. 또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다. 칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

**필요개념**

이 문제는 행 개수는 지정되어있으나, 열 개수는 불규칙한 배열을 다루는 문제였다.

우선 for문을 이용하여 한 문장씩 받고, 이를 char배열로 변환해 이중배열을 만들어주었고, 이후 출력할 떄 for문 작성을 위해 가장 긴 행 길이를 max 변수에 담았다.

출력할 땐 조건문으로 각 행마다 행 길이에 맞게 출력했다.

**정답코드**

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] arr = new char[5][];
        int max = 0;

        for (int i = 0; i < 5; i++) {
            String str = br.readLine();
            arr[i] = new char[str.length()];

            if (str.length() > max) max = str.length();
            for (int j = 0 ; j < arr[i].length ; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        for (int i = 0 ; i < max ; i++)  {
            for (int j = 0 ; j < 5 ; j++) {
                if (i < arr[j].length) System.out.print(arr[j][i]);
            }
        }

    }
}
```

---

### ✅ 문제 4 \_ 색종이 🌟🌟

**문제**

가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

**필요개념**

**정답코드**

```java

```
