# 백준 5단계

### **theme** - 문자열

<br>

### ✅ 문제 1 \_ 문자와 문자

**문제**

단어S와 정수i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.

**필요개념**

String에서 한 글자만 뽑아낼 때, 배열처럼 쓰면 안 되고 **string.charAt()**을 \*\*\*\*사용해야 한다!

**정답코드**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int size = sc.nextInt();
        System.out.println(str.charAt(size - 1));
    }
}
```

---

### ✅ 문제 2 \_ 단어 길이 재기

**문제**

알파벳으로만 이루어진 단어를 입력받아, 그 길이를 출력하는 프로그램을 작성하시오.

**필요개념**

String의 길이는 **length()**를 이용한다. 참고로 int형 배열, double형 배열 등의 배열은 **length** 메소드를 이용한다.

**정답코드**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(str.length());
    }
}
```

---

### ✅ 문제 3 \_ 문자열

**문제**

문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

**필요개념**

계속 런타임에러가 떠서 애를 먹었다,, ‘숫자 다음줄 문자열’ 의 형태라서 string을 받을 때 **sc.nextLine()**을 사용하면 개행만 가져온다고 한다,,,,, 그래서 이 점을 이용해 nextInt()로 문자를 먼저 받은 후, nextLine()으로 개행을 받아서 이후로는 string만 받을 수 있게 하려 했는데 생각해보니 3번의 string을 생성하는 것보다는 stringbuilder를 사용하는 것이 효율적이라고 생각해 **StringBuilder**를 사용했다!

- 📌 개인적으로 궁금해서 정리한 next()와 nextLine() 차이
  둘 다 string형을 받을 때 쓰는 메소드이지만 차이점이 있었다.
  - **next()** - 그냥 다음 토큰을 string으로 리턴하는 메소드. 분리자는 제외하고 읽어옴
  - **nextLine()** - 개행문자까지 읽어온다. 즉, 분리자도 다 읽어올 수 있다는 의미.예를 들어, 가<엔터> or 가나다 라마<엔터> 어떤식으로 입력이 되었든 <엔터> 까지 문자열을 모두 가져오게 된다. 물론 반환은 개행문자 이전 문자열만 반환된다.

**정답코드**

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String str = sc.next();
            sb.append(str.charAt(0));
            sb.append(str.charAt(str.length()- 1) + "\n");
        }
        System.out.print(sb);
    }
}
```

---

### ✅ 문제 4 \_ 아스키코드 🌟🌟

**문제**

알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

**필요개념**

사실 그냥 입력받은 것을 int형으로 출력하면 되는 문제이다. 그런데 한 글자를 받기 위해 Scanner를 이용하는 것이 비효율적이라는 내용을 보았다!

처음 안 사실이지만 System.in은 InputSstream 타입의 필드라고 한다. InputStream은 1byte만 읽어온다는 특징때문에 문자를 그대로 읽지 못하는 경우가 발생한다(특히 한글). 이때 문자형태 변환을 지원해주는 InputStreamReader를 사용한다.

InputStreamReader은 문자단위 데이터로 변환해준다. 하지만 “문자열”은 지원해주지 않아 문자열 입력을 원하면 배열을 선언해야 한다. 이러한 단점때문에 BufferedReader를 이용해 Buffer에 문자를 쌓아두고 문자열처럼 내보내는 방식으로 사용한다고 한다!

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```

즉 위 코드는 [System.in](http://System.in) = InputStream → InputStreamReader → BufferedReader 가 된다.

📌 **그렇다면 Scanner를 쓰는건 왜 비효율적?**

Scanner는 사용할 때 약 44줄의.. 정규식을 통과하여 검사한 후 반환한다. 그래서 속도가 느리기 때문에 시간 효율을 중요하게 생각하는 알고리즘에서는 BufferedReader가 선호될 수밖에 없다고 한다!

**정답코드**

1. Scanner 사용 (시간 200ms)

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.next().charAt(0);

        System.out.println(a);
    }
}
```

1. 한 글자만 처리하면 되므로 System.in만 사용 (시간 132ms)

```java
public class Main {
    public static void main(String[] args) throws Exception {

        int a = System.in.read();
        System.out.print(a);
    }
}
```

겨우 한 글자 처리에도 시간차이가 꽤 났다 😮

---

### ✅ 문제 5 \_ 숫자의 합

**문제**

**필요개념**

**정답코드**
