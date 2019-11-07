'''
    The oil properties for the sample oil named oil_bahia
    (Note: we put these things in their own separate file because
           some oil properties records can get quite large)
'''

json_data = {'name': 'oil_bahia',
             'adios_oil_id': 'AD00102',
             'api': 35.2,

             'saturates_fraction': None,
             'aromatics_fraction': None,
             'resins_fraction': None,
             'asphaltenes_fraction': None,

             'flash_point_min_k': None,
             'flash_point_max_k': 339.432,
             'pour_point_min_k': 310.9278,
             'pour_point_max_k': 310.9278,
             'oil_water_interfacial_tension_n_m': 0.02995,
             'oil_water_interfacial_tension_ref_temp_k': 288.15,
             'oil_seawater_interfacial_tension_n_m': None,
             'oil_seawater_interfacial_tension_ref_temp_k': None,

             'bullwinkle_time': None,
             'bullwinkle_fraction': 0.214734,
             'adhesion_kg_m_2': 0.035,
             'emulsion_water_fraction_max': 0.9,
             'solubility': 0.0,

             'benzene_fraction': None,
             'naphthenes_fraction': None,
             'paraffins_fraction': None,
             'polars_fraction': None,
             'sulphur_fraction': 0.0,
             'wax_content_fraction': None,
             'nickel_ppm': None,
             'vanadium_ppm': None,
             'k0y': 2.024e-06,

             'densities': [{'kg_m_3': 848.83, 'ref_temp_k': 288.15,
                            'weathering': 0.0}],
             'kvis': [{'m_2_s': 1.7e-05, 'ref_temp_k': 310.9278,
                       'weathering': 0.0}],
             'cuts': [{'liquid_temp_k': None, 'vapor_temp_k': 387.0105241,
                       'fraction': 0.188814933,
                       },
                      {'liquid_temp_k': None, 'vapor_temp_k': 482.1784523,
                       'fraction': 0.377629866,
                       },
                      {'liquid_temp_k': None, 'vapor_temp_k': 577.3463805,
                       'fraction': 0.566444799,
                       },
                      {'liquid_temp_k': None, 'vapor_temp_k': 672.5143087,
                       'fraction': 0.755259732,
                       },
                      {'liquid_temp_k': None, 'vapor_temp_k': 767.6822369,
                       'fraction': 0.944074665,
                       }],
             'molecular_weights': [{'g_mol': 108.074959,
                                    'ref_temp_k': 387.010524,
                                    'sara_type': 'Saturates'},
                                   {'g_mol': 94.8811238,
                                    'ref_temp_k': 387.010524,
                                    'sara_type': 'Aromatics'},
                                   {'g_mol': 165.524791,
                                    'ref_temp_k': 482.178452,
                                    'sara_type': 'Saturates'},
                                   {'g_mol': 149.081346,
                                    'ref_temp_k': 482.178452,
                                    'sara_type': 'Aromatics'},
                                   {'g_mol': 242.850128,
                                    'ref_temp_k': 577.346381,
                                    'sara_type': 'Saturates'},
                                   {'g_mol': 223.890452,
                                    'ref_temp_k': 577.346381,
                                    'sara_type': 'Aromatics'},
                                   {'g_mol': 349.24214,
                                    'ref_temp_k': 672.514309,
                                    'sara_type': 'Saturates'},
                                   {'g_mol': 330.298794,
                                    'ref_temp_k': 672.514309,
                                    'sara_type': 'Aromatics'},
                                   {'g_mol': 502.365797,
                                    'ref_temp_k': 767.682237,
                                    'sara_type': 'Saturates'},
                                   {'g_mol': 491.381014,
                                    'ref_temp_k': 767.682237,
                                    'sara_type': 'Aromatics'}],
             'sara_densities': [{'density': 1100.0,
                                 'ref_temp_k': 1015.0,
                                 'sara_type': 'Asphaltenes'},
                                {'density': 1100.0,
                                 'ref_temp_k': 1015.0,
                                 'sara_type': 'Resins'},
                                {'density': 633.692236,
                                 'ref_temp_k': 387.010524,
                                 'sara_type': 'Saturates'},
                                {'density': 681.878077,
                                 'ref_temp_k': 482.178452,
                                 'sara_type': 'Saturates'},
                                {'density': 724.073984,
                                 'ref_temp_k': 577.346381,
                                 'sara_type': 'Saturates'},
                                {'density': 761.853215,
                                 'ref_temp_k': 672.514309,
                                 'sara_type': 'Saturates'},
                                {'density': 796.216718,
                                 'ref_temp_k': 767.682237,
                                 'sara_type': 'Saturates'},
                                {'density': 760.430683,
                                 'ref_temp_k': 387.010524,
                                 'sara_type': 'Aromatics'},
                                {'density': 818.253692,
                                 'ref_temp_k': 482.178452,
                                 'sara_type': 'Aromatics'},
                                {'density': 868.888781,
                                 'ref_temp_k': 577.346381,
                                 'sara_type': 'Aromatics'},
                                {'density': 914.223857,
                                 'ref_temp_k': 672.514309,
                                 'sara_type': 'Aromatics'},
                                {'density': 955.460061,
                                 'ref_temp_k': 767.682237,
                                 'sara_type': 'Aromatics'}],
             'sara_fractions': [{'fraction': 0.0544039,
                                 'ref_temp_k': 1015.0,
                                 'sara_type': 'Resins'},
                                {'fraction': 0.0015214,
                                 'ref_temp_k': 1015.0,
                                 'sara_type': 'Asphaltenes'},
                                {'fraction': 0.0182564,
                                 'ref_temp_k': 387.010524,
                                 'sara_type': 'Saturates'},
                                {'fraction': 0.1705585,
                                 'ref_temp_k': 387.010524,
                                 'sara_type': 'Aromatics'},
                                {'fraction': 0.0,
                                 'ref_temp_k': 482.178452,
                                 'sara_type': 'Saturates'},
                                {'fraction': 0.1888149,
                                 'ref_temp_k': 482.178452,
                                 'sara_type': 'Aromatics'},
                                {'fraction': 0.0944075,
                                 'ref_temp_k': 577.346381,
                                 'sara_type': 'Saturates'},
                                {'fraction': 0.0944075,
                                 'ref_temp_k': 577.346381,
                                 'sara_type': 'Aromatics'},
                                {'fraction': 0.0944075,
                                 'ref_temp_k': 672.514309,
                                 'sara_type': 'Saturates'},
                                {'fraction': 0.0944075,
                                 'ref_temp_k': 672.514309,
                                 'sara_type': 'Aromatics'},
                                {'fraction': 0.0944075,
                                 'ref_temp_k': 767.682237,
                                 'sara_type': 'Saturates'},
                                {'fraction': 0.0944075,
                                 'ref_temp_k': 767.682237,
                                 'sara_type': 'Aromatics'}],
             'categories': [{'children': [],
                             'name': 'Light',
                             'parent': {'name': 'Crude'},
                             }],
             }
