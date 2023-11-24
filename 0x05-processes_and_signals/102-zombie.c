#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
* infinite_while - f
* Return: int
*/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - f
 * Return: 0
 */
int main(void)
{
int i;
pid_t zpid;

for (i = 0; i < 5; i++)
{
zpid = fork();
if (zpid)
{
printf("Zombie process created, PID: %i\n", zpid);
}
else
{
exit(0);
}
}
infinite_while();
return (0);
}
