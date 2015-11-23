/* Nohidy botnet scanner in c#  */
/* tries different scans to find various botnets */
/* works on http cuz its easy and this is a beta */
/* for more stuff visit:http://cybercrime-tracker.net/ */
#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <ctype.h>
#include <arpa/nameser.h>
#include <sys/stat.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>


void main(int argc, char *argv[])
{
 int sock,debugm=0;
 struct in_addr addr;
 struct sockaddr_in sin;
 struct hostent *he;
 unsigned long start;
 unsigned long end;
 unsigned long counter;
 char foundmsg[] = "200";
 char *botstr;
 char buffer[2048];  /*  2048 bytes should work for sockets  */
 int count=0;
 int numin;
 char botbuff[2048];
 char *buff[100];    
 char *botname[100]; 
 
 
 

 /* one little buf for one scan   */

 buff[1] = "GET /cp.php?m=login HTTP/1.0\n\n";
 buff[2] = "GET /helps/cp.php?m=login HTTP/1.0\n\n";
 buff[3] = "GET /cp.php?letter=login HTTP/1.0\n\n";    
 buff[4] = "GET /pony/admin.php HTTP/1.0\n\n";
 buff[5] = "GET /admin.php?do=auth HTTP/1.0\n\n";
 buff[6] = "GET /panelnew/admin.php HTTP/1.0\n\n";
 buff[7] = "GET /new/1/admin.php HTTP/1.0\n\n";
 buff[8] = "GET /web/adm/index.php?m=login HTTP/1.0\n\n";
 buff[9] = "GET /Panel/ HTTP/1.0\n\n";
 buff[10] = "GET /serverphp/cp.php?m=login HTTP/1.0\n\n";
 buff[11] = "GET /wp-admin/includes/saltonindex.php HTTP/1.0\n\n";
 buff[12] = "GET /modules/cp.php?m=login HTTP/1.0\n\n";
 buff[13] = "GET /login.php HTTP/1.0\n\n";
 buff[14] = "GET /solar/index.php?login  HTTP/1.0\n\n";
 buff[15] = "GET /panel/login.php  HTTP/1.0\n\n";
 buff[16] = "GET /panel/cp.php?m=login HTTP/1.0\n\n";
 buff[17] = "GET /adm/Panel/admin.php HTTP/1.0\n\n";
 buff[18] = "GET /admin/Panel/admin.php  HTTP/1.0\n\n";
 buff[19] = "GET /lc/ HTTP/1.0\n\n";
 buff[20] = "GET /panel/index.php?login  HTTP/1.0\n\n";
 buff[21] = "GET /pony/Panel/admin.php HTTP/1.0\n\n";
 buff[22] = "GET  HTTP/1.0\n\n";
 buff[23] = "GET  HTTP/1.0\n\n";
 buff[24] = "GET  HTTP/1.0\n\n";
  
botname[1] = "Zeus ";
botname[2] = "Citadel  ";
botname[3] = "Zeus ";
botname[4] = "Pony       ";
botname[5] = "H1N1 loader ";
botname[6] = "Pony ";
botname[7] = "PONY ";
botname[8] = "IceIX ";
botname[9] = "i think its Gorynych";
botname[10] = "Zeus ";
botname[11] = "Mailer ";
botname[12] = "Zeus ";
botname[13] = "might be Enslaver ";
botname[14] = "Solar ";
botname[15] = "might be kraken ";
botname[16] = "Citadel ";
botname[17] = "Pony ";
botname[18] = "Pony ";
botname[19] = "might be WebInject ";
botname[20] = "Solar ";
botname[21] = "Pony ";
botname[22] = " ";
botname[23] = " ";
botname[24] = " ";


if (argc<2)
   {
   printf("\n  Nohidy botnet scan in c#");
   printf("\nusage : %s just enter host ",argv[0]);
   printf("\n   Or : %s host -d   for debug mode\n\n",argv[0]); 
   exit(0);
   }

 if (argc>2)
   {
   if(strstr("-d",argv[2]))
     {
     debugm=1;
     }
   }

 if ((he=gethostbyname(argv[1])) == NULL)
   {
   herror("gethostbyname");
   exit(0);
   }

 printf("\n\n\t Nohidy botnet scan , scans Port 80");
 start=inet_addr(argv[1]);
 counter=ntohl(start);

   sock=socket(AF_INET, SOCK_STREAM, 0);
   bcopy(he->h_addr, (char *)&sin.sin_addr, he->h_length);
   sin.sin_family=AF_INET;
   sin.sin_port=htons(80);    
   
  if (connect(sock, (struct sockaddr*)&sin, sizeof(sin))!=0)
     {
     perror("connect");
     }
   printf("\n\n\t [ Press any key to check out the httpd version bro \n");
   getchar();     /* CKS  sorry, but ur new piece of code don't work :-( */
   send(sock, "HEAD / HTTP/1.0\n\n",17,0);
   recv(sock, buffer, sizeof(buffer),0);
   printf("%s",buffer);
   close(sock); 
  
   printf("\n\t [ Press any key to search");
   getchar();
   
while(count++ < 21)    /* 21 for 21 botscans */
   {
   sock=socket(AF_INET, SOCK_STREAM, 0);
   bcopy(he->h_addr, (char *)&sin.sin_addr, he->h_length);
   sin.sin_family=AF_INET;
   sin.sin_port=htons(80);
   if (connect(sock, (struct sockaddr*)&sin, sizeof(sin))!=0)
     {
     perror("connect");
     }
   printf("Searching for %s : ",botname[count]);
  
   for(numin=0;numin < 2048;numin++)
      {
      botbuff[numin] = '\0';
      } 
  
   send(sock, buff[count],strlen(buff[count]),0);
   recv(sock, botbuff, sizeof(botbuff),0);
   botstr = strstr(botbuff,foundmsg);
   if( botstr != NULL)
       printf("bingo i found it ;)\n");
   else
       printf("error could not find it , try changing host or the botnet is not in Nohidy syntax\n");
      
  if(debugm==1)
    { 
    printf("\n\n ------------------------\n %s \n ------------------------\n",botbuff); 
    printf("Press any key to continue....\n");         getchar();
    }  
   close(sock);
   }
   printf("take care \n");
 }

 
