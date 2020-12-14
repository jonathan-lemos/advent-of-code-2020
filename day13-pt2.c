#include <stdio.h>
#include <stdlib.h>

int nums[] = {29, 37, 433, 13, 17, 19, 23, 977, 41};
int indices[] = {0, 23, 29, 42, 43, 48, 52, 60, 101};

int main(void) {
	long long max = 1;

	for (size_t i = 0; i < sizeof(nums) / sizeof(nums[0]); ++i) {
		max *= nums[i];
	}

#pragma omp parallel
#pragma omp for
	for (long long i = 0; i <= max; i++) {
		int flag = 1;
		for (size_t j = 0; j < sizeof(nums) / sizeof(nums[0]); ++j) {
			if ((i + indices[j]) % nums[j] != 0) {
				flag = 0;
				break;
			}
		}
		if (flag) {
			printf("%lld\n", i);
			exit(0);
		}
	}

	return 0;
}
