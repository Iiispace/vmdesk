import gpu

GPUShaderCreateInfo = gpu.types.GPUShaderCreateInfo
GPUStageInterfaceInfo = gpu.types.GPUStageInterfaceInfo
create_from_info = gpu.shader.create_from_info


VERTEX_SOURCE_POS = '''
    void main() {
        pos = position;
        gl_Position = viewProjectionMatrix * vec4(position, 1.0f, 1.0f);
    }
'''

# GL_BOX ------------------------------------------------------------------------------------------------------

shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('VEC4', "color")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source('''
    void main() {
        gl_Position = viewProjectionMatrix * vec4(position, 1.0f, 1.0f);
    }
''')

shader_info.fragment_source('''
    void main() {
        FragColor = color;
    }
''')

GL_BOX = create_from_info(shader_info)
GL_BOX_bind = GL_BOX.bind
GL_BOX_uniform_float = GL_BOX.uniform_float

# GL_RIM ------------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('IVEC4', "inner")
shader_info.push_constant('VEC4', "color")
shader_info.push_constant('VEC4', "color_rim")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    void main() {
        if (pos[0] >= inner[0] && pos[0] <= inner[1] && pos[1] >= inner[2] && pos[1] <= inner[3])
            FragColor = color;
        else
            FragColor = color_rim;
    }
''')

GL_RIM = create_from_info(shader_info)
GL_RIM_bind = GL_RIM.bind
GL_RIM_uniform_float = GL_RIM.uniform_float
GL_RIM_uniform_int = GL_RIM.uniform_int

# GL_BUTTON ---------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('IVEC4', "inner")
shader_info.push_constant('INT', "state")
shader_info.push_constant('VEC4', "color")
shader_info.push_constant('VEC4', "color_rim")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    void main() {
        if (pos[0] >= inner[0] && pos[0] <= inner[1] && pos[1] >= inner[2] && pos[1] <= inner[3])
            FragColor = color;
        else {
            if (state > 1) {
                if (pos[1] >= inner[3] || pos[0] <= inner[0]) {
                    FragColor = vec4(color_rim[0], color_rim[1], color_rim[2], color_rim[3] * 0.35);
                    return;
                }
            } else {
                if (pos[1] <= inner[2] || pos[0] >= inner[1]) {
                    FragColor = vec4(color_rim[0], color_rim[1], color_rim[2], color_rim[3] * 0.3);
                    return;
                }
            }

            if (pos[0] >= inner[1]) {
                FragColor = vec4(color_rim[0], color_rim[1], color_rim[2], color_rim[3] * 0.4);
                return;
            }
            FragColor = color_rim;
        }
    }
''')

GL_BUTTON = create_from_info(shader_info)
GL_BUTTON_bind = GL_BUTTON.bind
GL_BUTTON_uniform_float = GL_BUTTON.uniform_float
GL_BUTTON_uniform_int = GL_BUTTON.uniform_int

# GL_BOXES_Y --------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('IVEC4', "T_T1_height_hideInd")
shader_info.push_constant('VEC4', "color")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    void main() {
        int yRelative = T_T1_height_hideInd[0] - int(pos[1]) ;
        int ind = yRelative / T_T1_height_hideInd[2] ;
        int y = T_T1_height_hideInd[0] + (yRelative - ind * T_T1_height_hideInd[2]) ;

        if (ind == T_T1_height_hideInd[3]) {
            FragColor = vec4(0.0f, 0.0f, 0.0f, 0.0f) ;
            return ;
        }

        if (y >= T_T1_height_hideInd[0] && y < T_T1_height_hideInd[1])
            FragColor = vec4(0.0f, 0.0f, 0.0f, 0.0f) ;
        else
            FragColor = color ;
    }
''')

GL_BOXES_Y = create_from_info(shader_info)
GL_BOXES_Y_bind = GL_BOXES_Y.bind
GL_BOXES_Y_uniform_float = GL_BOXES_Y.uniform_float
GL_BOXES_Y_uniform_int = GL_BOXES_Y.uniform_int

# GL_WIN ------------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('INT', "title_B")
shader_info.push_constant('VEC4', "color")
shader_info.push_constant('VEC4', "color_title")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    void main() {
        if (pos[1] <= title_B)
            FragColor = color;
        else
            FragColor = color_title;
    }
''')

GL_WIN = create_from_info(shader_info)
GL_WIN_bind = GL_WIN.bind
GL_WIN_uniform_float = GL_WIN.uniform_float
GL_WIN_uniform_int = GL_WIN.uniform_int

# GL_IMG ------------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "uvInterp")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.sampler(0, 'FLOAT_2D', "image")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_in(1, 'VEC2', "uv")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source('''
    void main() {
        uvInterp = uv;
        gl_Position = viewProjectionMatrix * vec4(position, 1.0f, 1.0f);
    }
''')

shader_info.fragment_source('''
    void main() {
        FragColor = texture(image, uvInterp);
    }
''')
GL_IMG = create_from_info(shader_info)
GL_IMG_bind = GL_IMG.bind
GL_IMG_uniform_float = GL_IMG.uniform_float
GL_IMG_uniform_sampler = GL_IMG.uniform_sampler

# GL_SHADOW ---------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('IVEC4', "inner")
shader_info.push_constant('INT', "d")
shader_info.push_constant('VEC4', "color")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    void main() {
        float x = pos[0];
        float y = pos[1];
        int L = inner[0];
        int R = inner[1];
        int B = inner[2];
        int T = inner[3];

        if (d == 0) {
            FragColor = color;
            return;
        }
        if (T < B) {
            FragColor = vec4(0.0, 0.0, 0.0, 0.0);
            return;
        }

        if (x >= L) {
            if (x <= R) {
                if (y >= B) {
                    if (y <= T) FragColor = color;
                    else {
                        int o = T + d;
                        FragColor = vec4(color[0], color[1], color[2], color[3] / (T - o) * (y - o));
                    }
                } else {
                    int o = B - d;
                    FragColor = vec4(color[0], color[1], color[2], color[3] / (B - o) * (y - o));
                }
            } else {
                if (y > T) {
                    int o = T + d;
                    int oo = R + d;
                    FragColor = vec4(color[0], color[1], color[2], color[3] / (T - o) * (y - o) / (R - oo) * (x - oo));
                    return;
                }
                if (y < B) {
                    int o = B - d;
                    int oo = R + d;
                    FragColor = vec4(color[0], color[1], color[2], color[3] / (B - o) * (y - o) / (R - oo) * (x - oo));
                    return;
                }
                int o = R + d;
                FragColor = vec4(color[0], color[1], color[2], color[3] / (R - o) * (x - o));
            }
        } else {
            if (y > T) {
                int o = T + d;
                int oo = L - d;
                FragColor = vec4(color[0], color[1], color[2], color[3] / (T - o) * (y - o) / (L - oo) * (x - oo));
                return;
            }
            if (y < B) {
                int o = B - d;
                int oo = L - d;
                FragColor = vec4(color[0], color[1], color[2], color[3] / (B - o) * (y - o) / (L - oo) * (x - oo));
                return;
            }
            int o = L - d;
            FragColor = vec4(color[0], color[1], color[2], color[3] / (L - o) * (x - o));
        }
    }
''')

GL_SHADOW = create_from_info(shader_info)
GL_SHADOW_bind = GL_SHADOW.bind
GL_SHADOW_uniform_float = GL_SHADOW.uniform_float
GL_SHADOW_uniform_int = GL_SHADOW.uniform_int

# GL_GRID -----------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('INT', "gridSize")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    void main() {
        FragColor = mod(floor(pos[0] / gridSize), 2.0) == mod(floor(pos[1] / gridSize), 2.0
            ) ? vec4(0.125977, 0.125977, 0.125977, 1.0) : vec4(0.358399, 0.358399, 0.358399, 1.0);
    }
''')

GL_GRID = create_from_info(shader_info)
GL_GRID_bind = GL_GRID.bind
GL_GRID_uniform_float = GL_GRID.uniform_float
GL_GRID_uniform_int = GL_GRID.uniform_int

# GL_PICKER_SV ------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('VEC4', "LRBT")
shader_info.push_constant('FLOAT', "hue")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    float L = LRBT[0] + 1.0;
    float B = LRBT[2] + 1.0;
    float s = (pos[0] - L) / (LRBT[1] - 1.0 - L);
    float v = (pos[1] - B) / (LRBT[3] - 1.0 - B);

    float r;
    float g;
    float b;

    float A[256] = float[](
        0.0,2.16e-05,4.33e-05,6.5e-05,
        8.6e-05,0.0001083,0.00012207030886202119,0.00023,
        0.00033,0.00042724607919808477,0.00058,0.0007324218458961695,
        0.001037597598042339,0.001342773379292339,0.0015,0.001647949160542339,
        0.001953124941792339,0.002258300664834678,0.002868652227334678,0.003173828008584678,
        0.003540038946084678,0.003845214727334678,0.004211425548419356,0.005004882579669356,
        0.005371093517169356,0.005859374767169356,0.006286620860919356,0.006713866954669356,
        0.007202148204669356,0.008300780784338713,0.008850097190588713,0.009399413596838713,
        0.010009765159338713,0.010620116721838713,0.011230468284338713,0.012695312034338713,
        0.013305663596838713,0.014038085471838713,0.014892577659338713,0.015624999534338713,
        0.016357420943677425,0.017211913131177425,0.018066405318677425,0.019775389693677425,
        0.020751952193677425,0.021728514693677425,0.022705077193677425,0.023681639693677425,
        0.024658202193677425,0.025634764693677425,0.026855467818677425,0.027832030318677425,
        0.030029295943677425,0.031249999068677425,0.03247070126235485,0.03369140438735485,
        0.03491210751235485,0.03613281063735485,0.03759765438735485,0.03881835751235485,
        0.04028320126235485,0.04150390438735485,0.04443359188735485,0.04589843563735485,
        0.04736327938735485,0.04882812313735485,0.05053710751235485,0.05200195126235485,
        0.05371093563735485,0.05517577938735485,0.05712890438735485,0.05859374813735485,
        0.06054687313735485,0.06201171688735485,0.0639648400247097,0.0673828087747097,
        0.0693359337747097,0.0712890587747097,0.0732421837747097,0.0751953087747097,
        0.0771484337747097,0.0791015587747097,0.0810546837747097,0.0834960900247097,
        0.0854492150247097,0.0874023400247097,0.0898437462747097,0.0917968712747097,
        0.0942382775247097,0.0964355431497097,0.0986328087747097,0.1035156212747097,
        0.1059570275247097,0.1083984337747097,0.1108398400247097,0.1132812462747097,
        0.1157226525247097,0.1181640587747097,0.1210937462747097,0.1235351525247097,
        0.1259765550494194,0.1289062425494194,0.1313476487994194,0.1342773362994194,
        0.1372070237994194,0.1396484300494194,0.1425781175494194,0.1455078050494194,
        0.1484374925494194,0.1513671800494194,0.1542968675494194,0.1572265550494194,
        0.1606445237994194,0.1669921800494194,0.1699218675494194,0.1728515550494194,
        0.1762695237994194,0.1796874925494194,0.1826171800494194,0.1860351487994194,
        0.1894531175494194,0.1928710862994194,0.1962890550494194,0.1997070237994194,
        0.2031249925494194,0.2070312425494194,0.2104492112994194,0.2138671800494194,
        0.2177734300494194,0.2216796800494194,0.2250976487994194,0.2285156175494194,
        0.2324218675494194,0.2363281175494194,0.2402343675494194,0.2441406175494194,
        0.2480468675494194,0.2519531100988388,0.2558593600988388,0.2602538913488388,
        0.2646484225988388,0.2685546725988388,0.2724609225988388,0.2763671725988388,
        0.2812499850988388,0.2851562350988388,0.289555,0.2939452975988388,
        0.2983398288488388,0.3027343600988388,0.307135,0.3115234225988388,
        0.3164062350988388,0.320805,0.3251952975988388,0.330085,
        0.3349609225988388,0.3398437350988388,0.3447265475988388,0.3486327975988388,
        0.3583984225988388,0.360845,0.3632812350988388,0.36866,
        0.3740234225988388,0.37891,0.3837890475988388,0.3945312350988388,
        0.39698,0.3994140475988388,0.4042968600988388,0.40967,
        0.4150390475988388,0.4208984225988388,0.4316406100988388,0.4365234225988388,
        0.4423827975988388,0.44532,0.4482421725988388,0.4531249850988388,
        0.4589843600988388,0.4648437350988388,0.47071,0.4765624850988388,
        0.48243,0.4882812350988388,0.494145,0.4999999850988388,
        0.50574,0.5114745795726776,0.517825,0.5241698920726776,
        0.5300292670726776,0.53638,0.5427245795726776,0.549075,
        0.5554198920726776,0.5612792670726776,0.5681152045726776,0.5739745795726776,
        0.5808105170726776,0.5876464545726776,0.5935058295726776,0.6003417670726776,
        0.6071777045726776,0.6140136420726776,0.6208495795726776,0.6267089545726776,
        0.6345214545726776,0.6403808295726776,0.6481933295726776,0.6550292670726776,
        0.6618652045726776,0.6687011420726776,0.6755370795726776,0.6833495795726776,
        0.6901855170726776,0.6970214545726776,0.7048339545726776,0.7126464545726776,
        0.7194823920726776,0.7263183295726776,0.7341308295726776,0.7419433295726776,
        0.7497558295726776,0.7565917670726776,0.7644042670726776,0.7712402045726776,
        0.7790527045726776,0.7868652045726776,0.7946777045726776,0.8024902045726776,
        0.8064,0.8103027045726776,0.8181152045726776,0.8269042670726776,
        0.8347167670726776,0.8435058295726776,0.8513183295726776,0.8591308295726776,
        0.8747558295726776,0.8845214545726776,0.8923339545726776,0.896245,
        0.9001464545726776,0.9089355170726776,0.9177245795726776,0.9255370795726776,
        0.9343261420726776,0.9431152045726776,0.9606933295726776,0.9646,
        0.9685058295726776,0.9782714545726776,0.9860839545726776,0.9958495795726776
    );

    void main() {
        if (s != 0.0) {
            int i = int (hue * 6.0);
            float f = hue * 6.0 - i;
            float p = v * (1.0 - s);
            float q = v * (1.0 - s * f);
            float t = v * (1.0 - s * (1.0 - f));
            i %= 6;

            if (i == 0){        r = v; g = t; b = p;
            } else if (i == 1){ r = q; g = v; b = p;
            } else if (i == 2){ r = p; g = v; b = t;
            } else if (i == 3){ r = p; g = q; b = v;
            } else if (i == 4){ r = t; g = p; b = v;
            } else {            r = v; g = p; b = q;
            }
        }

        FragColor = vec4(A[int(r*255)], A[int(g*255)], A[int(b*255)], 1.0);
    }
''')

GL_PICKER_SV = create_from_info(shader_info)
GL_PICKER_SV_bind = GL_PICKER_SV.bind
GL_PICKER_SV_uniform_float = GL_PICKER_SV.uniform_float

# GL_PICKER_H -------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('VEC4', "LRBT")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    float T = LRBT[3] - 1.0;
    float y = 6 * (pos[1] - T)/(T - LRBT[2] + 1.0) + 6;
    float r;
    float g;
    float b;

    float A[256] = float[](
        0.0,2.16e-05,4.33e-05,6.5e-05,
        8.6e-05,0.0001083,0.00012207030886202119,0.00023,
        0.00033,0.00042724607919808477,0.00058,0.0007324218458961695,
        0.001037597598042339,0.001342773379292339,0.0015,0.001647949160542339,
        0.001953124941792339,0.002258300664834678,0.002868652227334678,0.003173828008584678,
        0.003540038946084678,0.003845214727334678,0.004211425548419356,0.005004882579669356,
        0.005371093517169356,0.005859374767169356,0.006286620860919356,0.006713866954669356,
        0.007202148204669356,0.008300780784338713,0.008850097190588713,0.009399413596838713,
        0.010009765159338713,0.010620116721838713,0.011230468284338713,0.012695312034338713,
        0.013305663596838713,0.014038085471838713,0.014892577659338713,0.015624999534338713,
        0.016357420943677425,0.017211913131177425,0.018066405318677425,0.019775389693677425,
        0.020751952193677425,0.021728514693677425,0.022705077193677425,0.023681639693677425,
        0.024658202193677425,0.025634764693677425,0.026855467818677425,0.027832030318677425,
        0.030029295943677425,0.031249999068677425,0.03247070126235485,0.03369140438735485,
        0.03491210751235485,0.03613281063735485,0.03759765438735485,0.03881835751235485,
        0.04028320126235485,0.04150390438735485,0.04443359188735485,0.04589843563735485,
        0.04736327938735485,0.04882812313735485,0.05053710751235485,0.05200195126235485,
        0.05371093563735485,0.05517577938735485,0.05712890438735485,0.05859374813735485,
        0.06054687313735485,0.06201171688735485,0.0639648400247097,0.0673828087747097,
        0.0693359337747097,0.0712890587747097,0.0732421837747097,0.0751953087747097,
        0.0771484337747097,0.0791015587747097,0.0810546837747097,0.0834960900247097,
        0.0854492150247097,0.0874023400247097,0.0898437462747097,0.0917968712747097,
        0.0942382775247097,0.0964355431497097,0.0986328087747097,0.1035156212747097,
        0.1059570275247097,0.1083984337747097,0.1108398400247097,0.1132812462747097,
        0.1157226525247097,0.1181640587747097,0.1210937462747097,0.1235351525247097,
        0.1259765550494194,0.1289062425494194,0.1313476487994194,0.1342773362994194,
        0.1372070237994194,0.1396484300494194,0.1425781175494194,0.1455078050494194,
        0.1484374925494194,0.1513671800494194,0.1542968675494194,0.1572265550494194,
        0.1606445237994194,0.1669921800494194,0.1699218675494194,0.1728515550494194,
        0.1762695237994194,0.1796874925494194,0.1826171800494194,0.1860351487994194,
        0.1894531175494194,0.1928710862994194,0.1962890550494194,0.1997070237994194,
        0.2031249925494194,0.2070312425494194,0.2104492112994194,0.2138671800494194,
        0.2177734300494194,0.2216796800494194,0.2250976487994194,0.2285156175494194,
        0.2324218675494194,0.2363281175494194,0.2402343675494194,0.2441406175494194,
        0.2480468675494194,0.2519531100988388,0.2558593600988388,0.2602538913488388,
        0.2646484225988388,0.2685546725988388,0.2724609225988388,0.2763671725988388,
        0.2812499850988388,0.2851562350988388,0.289555,0.2939452975988388,
        0.2983398288488388,0.3027343600988388,0.307135,0.3115234225988388,
        0.3164062350988388,0.320805,0.3251952975988388,0.330085,
        0.3349609225988388,0.3398437350988388,0.3447265475988388,0.3486327975988388,
        0.3583984225988388,0.360845,0.3632812350988388,0.36866,
        0.3740234225988388,0.37891,0.3837890475988388,0.3945312350988388,
        0.39698,0.3994140475988388,0.4042968600988388,0.40967,
        0.4150390475988388,0.4208984225988388,0.4316406100988388,0.4365234225988388,
        0.4423827975988388,0.44532,0.4482421725988388,0.4531249850988388,
        0.4589843600988388,0.4648437350988388,0.47071,0.4765624850988388,
        0.48243,0.4882812350988388,0.494145,0.4999999850988388,
        0.50574,0.5114745795726776,0.517825,0.5241698920726776,
        0.5300292670726776,0.53638,0.5427245795726776,0.549075,
        0.5554198920726776,0.5612792670726776,0.5681152045726776,0.5739745795726776,
        0.5808105170726776,0.5876464545726776,0.5935058295726776,0.6003417670726776,
        0.6071777045726776,0.6140136420726776,0.6208495795726776,0.6267089545726776,
        0.6345214545726776,0.6403808295726776,0.6481933295726776,0.6550292670726776,
        0.6618652045726776,0.6687011420726776,0.6755370795726776,0.6833495795726776,
        0.6901855170726776,0.6970214545726776,0.7048339545726776,0.7126464545726776,
        0.7194823920726776,0.7263183295726776,0.7341308295726776,0.7419433295726776,
        0.7497558295726776,0.7565917670726776,0.7644042670726776,0.7712402045726776,
        0.7790527045726776,0.7868652045726776,0.7946777045726776,0.8024902045726776,
        0.8064,0.8103027045726776,0.8181152045726776,0.8269042670726776,
        0.8347167670726776,0.8435058295726776,0.8513183295726776,0.8591308295726776,
        0.8747558295726776,0.8845214545726776,0.8923339545726776,0.896245,
        0.9001464545726776,0.9089355170726776,0.9177245795726776,0.9255370795726776,
        0.9343261420726776,0.9431152045726776,0.9606933295726776,0.9646,
        0.9685058295726776,0.9782714545726776,0.9860839545726776,0.9958495795726776
    );

    void main() {
        if (y <= 1) {
            r = 1.0;
            g = y;
            b = 0.0;
        } else if (y <= 2) {
            r = 2.0 - y;
            g = 1.0;
            b = 0.0;
        } else if (y <= 3) {
            r = 0.0;
            g = 1.0;
            b = y - 2.0;
        } else if (y <= 4) {
            r = 0.0;
            g = 4.0 - y;
            b = 1.0;
        } else if (y <= 5) {
            r = y - 4.0;
            g = 0.0;
            b = 1.0;
        } else {
            r = 1.0;
            g = 0.0;
            b = 6.0 - y;
        }

        FragColor = vec4(A[int(r*255)], A[int(g*255)], A[int(b*255)], 1.0);
    }
''')

GL_PICKER_H = create_from_info(shader_info)
GL_PICKER_H_bind = GL_PICKER_H.bind
GL_PICKER_H_uniform_float = GL_PICKER_H.uniform_float

# GL_SELECTION ------------------------------------------------------------------------------------------------

vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.smooth('VEC2', "pos")
shader_info = GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('IVEC4', "inner")
shader_info.push_constant('INT', "gapSize")
shader_info.push_constant('VEC4', "color")
shader_info.push_constant('VEC4', "color_rim")
shader_info.vertex_in(0, 'VEC2', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(VERTEX_SOURCE_POS)

shader_info.fragment_source('''
    void main() {
        if (pos[0] >= inner[0] && pos[0] <= inner[1] && pos[1] >= inner[2] && pos[1] <= inner[3])
            return;
        else {
            int gap = gapSize == 0 ? 1 : gapSize;
            FragColor = mod(floor(pos[0] / gap), 2.0) == mod(floor(pos[1] / gap), 2.0
            ) ? color : color_rim;
        }
    }
''')

GL_SELECTION = create_from_info(shader_info)
GL_SELECTION_bind = GL_SELECTION.bind
GL_SELECTION_uniform_float = GL_SELECTION.uniform_float
GL_SELECTION_uniform_int = GL_SELECTION.uniform_int

# GL_SCREENDASH_3D ------------------------------------------------------------------------------------------------
# https://github.com/blender/blender/blob/blender-v4.3-release/source/blender/gpu/shaders/infos/gpu_shader_line_dashed_uniform_color_info.hh
vert_out = GPUStageInterfaceInfo("temp_interface")
vert_out.no_perspective("VEC2", "stipple_start")
vert_out.flat("VEC2", "stipple_pos")

shader_info = GPUShaderCreateInfo()
shader_info.vertex_in(0, "VEC3", "pos")
push_constant = shader_info.push_constant
push_constant("MAT4", "ModelViewProjectionMatrix")
push_constant("VEC2", "viewport_size")
push_constant("FLOAT", "dash_width")
push_constant("VEC4", "color")
push_constant("VEC4", "color2")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, "VEC4", "fragColor")

# https://github.com/blender/blender/blob/blender-v4.3-release/source/blender/gpu/shaders/gpu_shader_3D_line_dashed_uniform_color_vert.glsl
shader_info.vertex_source('''
    void main() {
        vec4 pos_4d = vec4(pos, 1.0);
        gl_Position = ModelViewProjectionMatrix * pos_4d;
        stipple_start = stipple_pos = viewport_size * 0.5 * (gl_Position.xy / gl_Position.w);
    }
''')

# https://github.com/blender/blender/blob/blender-v4.3-release/source/blender/gpu/shaders/gpu_shader_2D_line_dashed_frag.glsl
shader_info.fragment_source('''
    void main() {
        if (fract(distance(stipple_pos, stipple_start) / dash_width) <= 0.5) {
            fragColor = color;
        } else {
            fragColor = color2;
        }
    }
''')

GL_SCREENDASH_3D = create_from_info(shader_info)
GL_SCREENDASH_3D_bind = GL_SCREENDASH_3D.bind
GL_SCREENDASH_3D_uniform_float = GL_SCREENDASH_3D.uniform_float

# -------------------------------------------------------------------------------------------------------------

del vert_out
del push_constant
del shader_info