#include <stdio.h>
#include <stdlib.h>

int main(){
	char name[127];
	char callmkg3a[255] = ".\\\\mkg3a -n basic:";
	fprintf(stdout, "Enter the project name: ");
	fscanf(stdin, "%s", name);
	strncat(callmkg3a, name, 20);
	strncat(callmkg3a, " -i uns:.\\\\", 20);
	strncat(callmkg3a, name, 20);
	strncat(callmkg3a, "\\unselected.bmp -i sel:.\\\\", 30);
	//printf("\\\\"); //testing how many escape slashes we need to get two actual slashes
	strncat(callmkg3a, name, 20);
	strncat(callmkg3a, "\\selected.bmp .\\\\", 30);
    strncat(callmkg3a, name, 20);
    strncat(callmkg3a, "\\", 20);
    strncat(callmkg3a, name, 20);
    strncat(callmkg3a, ".bin .\\\\", 20);
    strncat(callmkg3a, name, 20);
//    strncat(callmkg3a, "\\", 20);
//    strncat(callmkg3a, name, 20);
    strncat(callmkg3a, "\\", 20);
    strncat(callmkg3a, name, 20);
    strncat(callmkg3a, ".g3a", 20);
	fprintf(stdout, "\n%s\n\n", callmkg3a);
	system(callmkg3a);
	system("pause");
//.\\mkg3a -n basic:example -i uns:C:\mkg3a\example\unselected.bmp -i sel:C:\mkg3a\example\unselected.bmp C:\
mkg3a\example\example.bin C:\mkg3a\example\example.g3a
    return 0;
}
