#!/usr/bin/env python3
import numpy as np

class ConvolutionNeuron:
    
    def __init__( self ):
        self.weights = np.array([
                                 [ 0, 1, 0 ],
                                 [ 0, 1, 0 ],
                                 [ 0, 1, 0 ]
                               ])

    def forward( self, X ):
        return X * self.weight

    def __call__( self, X ):
        return self.forward( X )


Y = []

X = np.array ([
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])


weights = np.array ([
                     [ 0, 1, 0 ],
                     [ 0, 1, 0 ],
                     [ 0, 1, 0 ]
                   ])
#neuron = ConvolutionNeuron()
conv1 = np.random.randn( 6, 7 )

print( f"\narray X >>>\n{X}" )
print( f"\nweights >>>\n{weights}")



x_0 = X[:3]
print( f"\nx_0 >>>\n{x_0}" )
x_0_0 = x_0[ 0:3, 0:3 ]
print( f"\nx_0_0 >>>\n{x_0_0}" )
y_0 = x_0_0 * weights
print( f"\ny_0 >>>{y_0}" )

conv1[0][0] = y_0

x_1 = X[1:4]
print( f"\nx_1 >>>\n{x_1}" )
x_1_0 = x_1[ 0:3, 0:3 ]
print( f"\nx_1_0 >>>\n{x_1_0}" )
y_0 = x_1_0 * weights
print( y_0 )

print( conv1 )



