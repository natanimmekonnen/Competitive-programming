public class DefanginganIPAddress {

    public String defangIPaddr(String address) {
        char[] addres= address.toCharArray();
        StringBuilder newstring= new StringBuilder();
        for(char s:addres)
        {
            if(s=='.')
            {
                newstring.append("[.]");

            }
            else
            {
                newstring.append(s);
            }
        }
        return newstring.toString();

    }
}
}
