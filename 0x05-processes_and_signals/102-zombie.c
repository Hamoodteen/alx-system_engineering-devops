#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

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
sleep(100);
return (0);
}
