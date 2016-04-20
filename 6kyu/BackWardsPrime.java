import java.util.*;

public class BackWardsPrime
{
    public static void main(String[] args)
    {
        System.out.println(backwardsPrime(2, 100));
    }

    public static String backwardsPrime(long start, long end)
    {
        long size = start - end;
        ArrayList<Long> arr = new ArrayList<Long>();
        long i;
        for(i = start; i <= end; i++)
        {
            arr.add(i);
        }
        Object[] objArr = arr.toArray();
        String[] strArr = Arrays.copyOf(objArr, objArr.length, String[].class);
        return Arrays.toString(strArr);
    }
}
