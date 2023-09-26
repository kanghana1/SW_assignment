# 백준 6단계

### **theme** - 심화1

<br>

### ✅ 문제 1 \_ 새싹

**문제**
아래 예제와 같이 새싹을 출력하시오.

```java
         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |
```

**필요개념**

따옴표 안에 따옴표를 출력할 떄는 \를 끼워넣어줘야 한다! 그리고 \를 출력할 떈 이거 앞에도 \를 끼워넣으면 된다. 이것만 알고 있으면 쉽게 출력이 가능하다.

**정답코드**

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("         ,r'\"7");
        System.out.println("r`-_   ,'  ,/");
        System.out.println(" \\. \". L_r'");
        System.out.println("   `~\\/");
        System.out.println("      |");
        System.out.println("      |");
    }
}
```

---

### ✅ 문제 2 \_ 킹, 퀸, 룩, 비숍, 나이트, 폰

**문제**

동혁이는 오래된 창고를 뒤지다가 낡은 체스판과 피스를 발견했다.

체스판의 먼지를 털어내고 걸레로 닦으니 그럭저럭 쓸만한 체스판이 되었다. 하지만, 검정색 피스는 모두 있었으나, 흰색 피스는 개수가 올바르지 않았다.

체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

동혁이가 발견한 흰색 피스의 개수가 주어졌을 때, 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.

**필요개념**

마찬가지로 BufferedReader를 사용했고, 한 문장 단위로 받은 후 **split()**을 이용해 숫자를 배열로 받았다!

이후에는 뺄셈을 이용해 답을 구했고, stream으로 프린트했다! **forEach 안에 람다식 쓸 수 있는 거** 잊지 말기!

**정답코드**

```java
import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String n = br.readLine();
        String[] arr = n.split(" ");
        int[] ans = {1, 1, 2, 2, 2, 8};
        int[] sol = new int[6];
        for (int i = 0; i < ans.length; i++) {
            sol[i] = ans[i] - Integer.parseInt(arr[i]);
        }

        Arrays.stream(sol).forEach(i -> System.out.print(i + " "));
    }
}
```

---

### ✅ 문제 3 \_ 별 찍기 - 7

**문제**

```java
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

규칙을 유추한 뒤 별을 찍어보세요

**필요개념**

가로로 반을 잘라서 생각했다! 공백을 n-1개 출력한 후 별 1개, 공백 n-2개 출력 후 별 2개... 이런식으로 생각하면서 코드를 구성했다.

이중for문밖에 방법이 없을 거 같긴 한데,, 다르게 푼 사람이 있을지 궁금하다!

**정답코드**

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        for (int i = 0; i < n; i++) {
            for (int j = n - 1 ; j > i; j--) {
                System.out.print(" ");
            }
            for (int j = 0 ; j < 2 * i + 1 ; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i = n - 1 ; i > 0 ; i--) {
            for (int j = n - 1 ; j >= i ; j--) {
                System.out.print(" ");
            }
            for (int j = 2 ; j < 2 * i + 1 ; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
```

---

### ✅ 문제 4 \_ 팰린드롬인지 확인하기

**문제**

알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

**필요개념**

인덱스를 활용해야 하기 때문에, 변수 l을 length() - 1 로 잡았다. String을 반으로 잘라서 i와 l - i 를 비교하는 작업을 했다. 비교 후 같으면 cnt에 1씩 더했다.

길이가 짝수인 문자열은 올림을 해줘야해서 Math.ceil() 메소드를 이용했다. 이때 함수 내부에 넣는 숫자는 double형이어야 한다! (이거때문에 좀 헤맸음)

**정답코드**

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String n = reader.readLine();
        int l = n.length() - 1;

        int cnt = 0;

        for (int i = 0 ; i <= l / 2 ; i++) {
            if ((i != l - i) && (n.charAt(i) == n.charAt(l - i))) cnt++;
        }
        if (cnt == Math.ceil((double) l / 2)) System.out.println(1);
        else System.out.println(0);
    }
}

```

---

### ✅ 문제 5 \_ 단어 공부 🌟🌟

**문제**

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다

**필요개념**

대소문자 구분 없고 출력은 대문자로 하기 때문에 받은 문자열을 **toUpperCase()** 메소드를 이용하여 대문자로 바꾸었다.

이후 알파벳 개수만큼의 사이즈를 갖는 int형 배열을 만들어 0으로 채워넣은 후, 나오는 알파벳의 자리 값을 1씩 더해갔다. 이 과정에서 아스키코드 (A가 65라는 점)을 이용했다.

다음 반복문으로 최댓값과 그의 인덱스를 구하고, 또 다른 반복문으로는 max와 같은 값이 또 있는가 즉, 최댓값이 2개 이상 있는가를 확인하여 문제를 풀었다.

근데코드도 너무 길고, 단순 반복문도 너무 많이 사용해 지저분한 느낌이었다. 다른 방법이 있을지 궁금하다!!!

**정답코드**

```java
import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String ans = br.readLine().toUpperCase();
        int[] eng = new int[26];
        Arrays.fill(eng,0);

        for (int i = 0 ; i < ans.length() ; i++) {
            eng[ans.charAt(i) - 65]++;
        }
        int max = -1;
        int index = -1;

        for (int i = 0 ; i < eng.length ; i++) {
            if (eng[i] > max) {
                max = eng[i];
                index = i;
            }
        }
        int cnt = -1;
        for (int i = 0 ; i < eng.length ; i++) {
            if (max == eng[i]) cnt++;
        }

        if (cnt != 0) System.out.println("?");
        else System.out.println((char)(65 + index));
    }
}
```

---

### ✅ 문제 6 \_ 크로아티아 알파벳 🌟🌟

**문제**

예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

크로아티아 알파벳 / 변경

č / c=

ć / c-

dž / dz=

đ / d-

lj / lj

nj / nj

š / s=

ž / z=

예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

**필요개념**

우선 크로아티아를 변경한 단어들을 String 배열로 만들어 넣어두었다. 알파벳 개수를 셀 때, 위 표에 없는 알파벳 개수도 써야한다는 걸 간과해서 계속 해맸다,,, boolean 변수를 만들어서 그냥 단어와 크로아티아 단어를 구분했다. (크로아티아 단어면 그 단어 길이만큼 스킵해야하니까)

그리고 String은 객체이므로 ==를 사용할 수 없고 **equals()** 메소드를 사용해야 한다는거 절대 잊지말기... 맨날 까먹음;;

**정답코드**

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String ans = br.readLine();
        String[] s = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

        int cnt = 0;
        int i = 0;
        while (i < ans.length()) {
            boolean found = false;
            for (int j = 0; j < s.length; j++) {
                if (i + s[j].length() <= ans.length() && ans.substring(i, i + s[j].length()).equals(s[j])) {
                    cnt++;
                    i += s[j].length();
                    found = true;
                    break;
                }
            }
            if (!found) {
                cnt++;
                i++;
            }
        }
        System.out.print(cnt);
    }
}
```
