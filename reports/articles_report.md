# Alguns resumos dos artigos de pesquisa

## [A Statistical Prediction Model Based on Sparse Representations for Single Image Super-Resolution](https://ieeexplore.ieee.org/abstract/document/6739068)

[Um link para uma explicação do artigo no youtube](https://www.youtube.com/watch?v=7FUHte0RTTI)

O artigo é fechado (sua distribuição não é gratúita), mas vi ser necessário demonstrar o mesmo pela tangente que o artigo escolhido para ser apresentado faz; por se tratar de um modelo de super-resolução em uma única imagem que foi considerado um dos melhores antes da publicação artigo sobre SRCNN (o artigo do repositório), e tendo em vista que ele tem o mesmo objetivo e mais ou menos a mesma metodologia. O presente consegue uma aproximação estatística com representação esparsa (que é uma representação dos dados com o mínimo de valores possíveis — [uma melhor explicação](https://dsp.stackexchange.com/questions/47726/what-exactly-is-sparse-representation)) da imagem. Em suma, ele realiza predições sobre determinados atributos da imagem baseando-se em sua representação esparsa. Ele tem em sua implementação uma *Restricted Boltzman machine*, que consegue aprender distribuição probabilística com a entrada do programa.

[Link para uma melhor aprofundamento sobre *sparse coding*](https://www.youtube.com/watch?v=7a0_iEruGoM)

## [A Fully Progressive Approach to Single-Image Super-Resolution](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Wang_A_Fully_Progressive_CVPR_2018_paper.html)

[Link do pdf](https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w13/Wang_A_Fully_Progressive_CVPR_2018_paper.pdf)

[Link do Github](https://github.com/fperazzi/proSR)