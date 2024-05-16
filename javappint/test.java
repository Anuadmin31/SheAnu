package javappint;

public class test {
    public static void main(String[]args){
        encap j = new encap();
        j.setacc_no(789074346798L);
        j.setamount(127834);
        j.setname("Anushri");
        j.setemail("anushrichinchankar@gmail.com");

        System.out.println(j.setacc_no()+" "+j.getemail()+" "+j.getname()+" "+j.gteamount());
    }
    
}
