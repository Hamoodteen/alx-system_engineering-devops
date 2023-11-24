#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

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
printf("Zombie process created, PID: %d\n", getpid());
exit(EXIT_SUCCESS);
}
}
sleep(1);
return (0);
}
