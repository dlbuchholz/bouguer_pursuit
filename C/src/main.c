#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    double x;
    double y;
} Point;

const double N = 0.75;

/* approx course
 * ---------------
 * Recursive function which approximates course of a pirate ship tailing a merchant ship
 *
 * INPUT:
 * k       | iterator
 * t       | current time
 * delta_t | time delta
 * pos_h   | position of merchant ship
 * pos_p   | position of pirate ship
 * angle   | arctan angle of pirate ship towards merchant ship
 * delta_x | delta
 *
 * OUTPUT: None */
void approx_course(size_t k, double t, double delta_t, Point ph, Point pp,
                   double angle, double delta_x, double delta_y,
                   double epsilon) {
                    ph.y = k * N * delta_t;
                    t = k * delta_t;
                    pp.x += delta_x;
                    pp.y += delta_y;
                    double tan = (double) (ph.y - pp.y) / (double) (1 - pp.x);

                    if(pp.x > ph.x + 1) {
                        printf("Distance is never below specified epsilon threshold!");
                        abort();
                    }

                    angle = atan(tan);
                    delta_x = delta_t * cos(angle);
                    delta_y = delta_t * sin(angle);

                    if((fabsl(ph.x - pp.x) < epsilon)
                    && (fabsl(ph.y - pp.y) < epsilon)) {
                        printf("th0: %f, yh0: %f", t, ph.y);
                    } else {
                        approx_course(k+1, t, delta_t, ph, pp, angle, delta_x, delta_y, epsilon);
                    }
}


int main (int argc, char** argv) {
    double delta_t = 0.000001;
    double epsilon = 0.000005;

    Point position_merchants = {.x = 1, .y = 0};
    Point position_pirates = {.x = 0, .y = 0};

    approx_course(0, 0, delta_t, position_merchants, position_pirates, 0, 0, 0, epsilon);
    return 0;
}