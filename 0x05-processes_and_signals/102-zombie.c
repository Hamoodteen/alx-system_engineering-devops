#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

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
* Return: int
*/
int main()
{
int num_zombies = 5;
pid_t child_pid;
for (int i = 0; i < num_zombies; ++i)
{
child_pid = fork();
if (child_pid == -1)
{
perror("Fork failed");
exit(EXIT_FAILURE);
}
if (child_pid > 0)
{
printf("Zombie process created, PID: %d\n", getpid());
}
else
{
infinite_while();
}
}
sleep(1);
return (0);
}
