import PySimpleGUI as sg
import mvector

col1 = [
       [sg.Text('vector 1'),sg.InputCombo(('cartesian', 'angle'), key='typev1', size=(12, 3)),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v1mag'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v1x'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v1y'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v1z')
        ],      
       [sg.Text('vector 2'),sg.InputCombo(('cartesian', 'angle'), key='typev2', size=(12, 3)), 
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v2mag'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v2x'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v2y'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v2z')
        ], 
       [sg.Text('vector 3'),sg.InputCombo(('cartesian', 'angle'), key='typev3', size=(12, 3)), 
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v3mag'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v3x'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v3y'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v3z')
        ]
        ]

col2 = [
       [sg.Text('vector 4'),sg.InputCombo(('cartesian', 'angle'), key='typev4', size=(12, 3)),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v4mag'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v4x'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v4y'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v4z')
        ],      
       [sg.Text('vector 5'),sg.InputCombo(('cartesian', 'angle'), key='typev5', size=(12, 3)), 
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v5mag'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v5x'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v5y'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v5z')
        ],
       [sg.Text('vector 6'),sg.InputCombo(('cartesian', 'angle'), key='typev6', size=(12, 3)), 
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v6mag'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v6x'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v6y'),
            sg.Input('0', size=(9, 3), do_not_clear=True, key='v6z')
        ]
        ]

layout = [
          [sg.Text('Vector Math')],
          [sg.Text('operation:'),
                sg.InputCombo(('addition', 'subtraction', 'dot product', 'cross product', 'unit vector'),key='mode', size=(12, 3))], 
          [sg.Column(col1), sg.Column(col2)],
          [sg.Submit(), sg.Cancel()], 
          [sg.Text('Vector:'), sg.Text('', size=(40, 1),   key='_OUTPUT1_'), sg.Text('', size=(40, 1), key="_OUTPUT2_")] 
         ]

window = sg.Window('Vector Math').Layout(layout)
while(True):
    button, values = window.Read()
    if (button == None or button == "Cancel"):
        break
    elif(button == 'Submit'):
        vectors = {}
        
        for key, value in values.items():
            if(key.startswith('type')):
                vStr = key[4:]
                tempV = mvector.Vector()
                
                if(value=='angle'):
                    tempV.set_by_angle(
                        float(values[vStr+'mag']), alpha=float(values[vStr+'x']) or None,
                        beta=float(values[vStr+'y']) or None, gamma=float(values[vStr+'z']) or None
                        )
                else:
                    tempV.set_xyz(
                        (float(values[vStr+'x']), float(values[vStr+'y']), float(values[vStr+'z']))
                        )
                
                vectors[vStr] = tempV
    
        v1 = mvector.add_vector(vectors['v1'].xyz(), vectors['v2'].xyz(), vectors['v3'].xyz())
        v2 = mvector.add_vector(vectors['v4'].xyz(), vectors['v5'].xyz(), vectors['v6'].xyz())
        
    
        if(values['mode'] == 'addition'):
            vector = mvector.add_vector(v1, v2)
        elif(values['mode'] == 'subraction'):
            vector = mvector.add_vector(v1, -v2)
        elif(values['mode'] == 'dot product'):
            vector = mvector.dot_product(v1, v2)
        elif(values['mode'] == 'cross product'):
            vector = mvector.cross_product(v1, v2)
        elif(values['mode'] == 'unit vector'):
            try:
                vector = mvector.scale_vector(vectors['v1'].xyz(), 1/vectors['v1'].magnitude())
            except ZeroDivisionError:
                vector = (0, 0, 0)
        else:
            vector = (0, 0, 0)
        
        if(values['mode'] != 'dot product'):
            vec = mvector.Vector(vector)
            vecCoordString = '[{0:.4f}, {1:.4f}, {2:.4f}]'.format(float(vector[0]), vector[1], vector[2])
            vecAngleString = 'mag:{0:.4f}; a:{1:7.4f}; b:{2:7.4f}; g:{3:7.4f}'.format(
                                                                                                                                  vec.magnitude(), 
                                                                                                                                  vec.angle('alpha'),
                                                                                                                                  vec.angle('beta'),
                                                                                                                                  vec.angle('gamma')
                                                                                                                                  )
            print(vecCoordString)
            print(vecAngleString)
            window.FindElement('_OUTPUT1_').Update(vecCoordString)
            window.FindElement('_OUTPUT2_').Update(vecAngleString)
        else:
            vecCoordString = '{0:.4f} (scalar)'.format(vector)
            vecAngleString = ''
        
        print(vecCoordString)
        print(vecAngleString)
        window.FindElement('_OUTPUT1_').Update(vecCoordString)
        window.FindElement('_OUTPUT2_').Update(vecAngleString)

window.Close()
