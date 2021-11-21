# Alguns resumos dos artigos de pesquisa

## [A Statistical Prediction Model Based on Sparse Representations for Single Image Super-Resolution](https://ieeexplore.ieee.org/abstract/document/6739068)

[Um link para uma explicação do artigo no youtube](https://www.youtube.com/watch?v=7FUHte0RTTI)

[Link do issue](https://github.com/ghastcmd/dip/issues/1)

O artigo é fechado (sua distribuição não é gratúita), mas vi ser necessário demonstrar o mesmo pela tangente que o artigo escolhido para ser apresentado faz; por se tratar de um modelo de super-resolução em uma única imagem que foi considerado um dos melhores antes da publicação artigo sobre SRCNN (o artigo do repositório), e tendo em vista que ele tem o mesmo objetivo e mais ou menos a mesma metodologia. O presente consegue uma aproximação estatística com representação esparsa (que é uma representação dos dados com o mínimo de valores possíveis — [uma melhor explicação](https://dsp.stackexchange.com/questions/47726/what-exactly-is-sparse-representation)) da imagem. Em suma, ele realiza predições sobre determinados atributos da imagem baseando-se em sua representação esparsa. Ele tem em sua implementação uma *Restricted Boltzman machine*, que consegue aprender distribuição probabilística com a entrada do programa.

[Link para uma melhor aprofundamento sobre *sparse coding*](https://www.youtube.com/watch?v=7a0_iEruGoM)

## [A Fully Progressive Approach to Single-Image Super-Resolution](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Wang_A_Fully_Progressive_CVPR_2018_paper.html)

[Link do pdf](https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w13/Wang_A_Fully_Progressive_CVPR_2018_paper.pdf)

[Link do Github](https://github.com/fperazzi/proSR)

[Link do issue](https://github.com/ghastcmd/dip/issues/2)

O paper consegue demonstrar uma super resolução em uma única imagem utilizando a técnica progressiva de geração. Em suma, o que a técnica significa é que ele vai progressivamente aumentando resolvendo a tarefa, de modo que cada tarefa é algo fácil de ser resolvido, ou seja, para o nosso contexto, ela vai aumentando gradativamente a resolução até que consiga chegar no nosso resultado esperado. O artigo evidencia o uso de uma rede que consegue subtrair os serrilhados causados pelo escalonamento da imagem de baixa resolução para uma imagem maior (até 8 vezes maior), e depois que a imagem passa por essa rede, ela vai para uma rede adversária generativa que consegue implementar os detalhes menores, que dão mais resolução à imagem.

## [Learning Temporal Coherence via Self-Supervision for GAN-based Video Generation (TecoGAN)](https://ge.in.tum.de/publications/2019-tecogan-chu/)

[Link do pdf](https://arxiv.org/pdf/1811.09393.pdf)

[Link do Github](https://github.com/thunil/TecoGAN)

[Link do issue](https://github.com/ghastcmd/dip/issues/3)

O presente artigo perfoma a façanha de aumentar a resolução (técnica de super resolução) com coerência temporal, ou seja, consegue performar aumento de resolução em imagens sequenciais, um vídeo, por assim dizer. Ele o realiza com a utilização de uma rede neural generativa, que diferente dos outros métodos que utilizam a mesma técnica de rede neural, consegue fazer a super resolução gerando muito poucos artefatos, ou então nenhum artefato, além de aprensetar maiores acréssimos de detalhes em comparação com outros métodos que realizam a mesma coisa. Além disso, ele consegue melhorar simulações física de partículas, em que outras técnicas de melhoramento dessas simulações precisavam ter um certo conhecimento de alguns parâmetros das partículas como velocidade, volume, esparsidade, porém, a presente técnica precisa somente das informações contidas na própria imagem do vídeo e já consegue performar melhor que a majoritariedade das outras técnicas anteriores.

## [RAISR: Rapid and Accurate Image Super Resolution](https://arxiv.org/abs/1606.01299)

[Link do pdf](https://arxiv.org/pdf/1606.01299.pdf)

[Link do video](https://www.youtube.com/watch?v=WovbLx8C0yA)

[Link do issue](https://github.com/ghastcmd/dip/issues/4)

O paper utiliza técnicas de aprendizado de máquina (sem ser a rede neural) para conseguir realizar o upscaling (aumentar a imagem), para uma resolução maior, e, talvez, conseguir adicionar mais detalhes a elas, uma vez que elas se apresentam em um estado empobrecido devido ao escalonamento anterior que degradou parte da informação da imagem. Não é para a técnica ser confundida com *Image Inpainting*, que é uma técnica que substitui uma parte da imagem baseada nos arredores da mesma. O algoritmo do artigo é altamente rápido e apresentou resultados superiores aqueles do artigo que estamos apresentando, além de ser melhor que os métodos manuais, para citar alguns: Nearest-Neighbor, SRCNN, A+.

## [Generative Adversarial Networks: An Overview](https://ieeexplore.ieee.org/abstract/document/8253599)

[Link do pdf](https://arxiv.org/pdf/1710.07035.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/5)

O artigo explica o que é uma rede neural adversarial generativa, e suas principais aplicações; no final ela mostra vários outros *papers* que utilizam a técnica para as mais diversas aplicações. O que é uma rede neural generativa adversarial? Basicamente é uma rede que contém uma parde que gera (a rede generativa), e a parte da rede que diz se a determinada saída da rede generativa é real ou não, ou seja se foi gerada artificialmente ou não (essa parte da rede é chamada de rede descriminadora). Com esse empasse entre gerar uma saída e dizer se ela é real ou não, a rede vai aprendendo cada vez mais, tanto a como detectar uma imagem falsa, quanto a gerar uma imagem cada vez mais real.

## [Accelerating the Super-Resolution Convolutional Neural Network](https://link.springer.com/chapter/10.1007/978-3-319-46475-6_25)

[Linkdo pdf](https://link.springer.com/content/pdf/10.1007%2F978-3-319-46475-6_25.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/6)



## [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://openaccess.thecvf.com/content_cvpr_2017/html/Ledig_Photo-Realistic_Single_Image_CVPR_2017_paper.html)

[Link do pdf](https://openaccess.thecvf.com/content_cvpr_2017/papers/Ledig_Photo-Realistic_Single_Image_CVPR_2017_paper.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/7)



## [Fast and Accurate Single Image Super-Resolution via Information Distillation Network](https://openaccess.thecvf.com/content_cvpr_2018/html/Hui_Fast_and_Accurate_CVPR_2018_paper.html)

[Link do pdf](https://openaccess.thecvf.com/content_cvpr_2018/papers/Hui_Fast_and_Accurate_CVPR_2018_paper.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/8)

## [Coupled Deep Autoencoder for Single Image Super-Resolution](https://ieeexplore.ieee.org/abstract/document/7339460)

[Link do pdf](https://www.researchgate.net/profile/Zeng-Kun-2/publication/284755272_Coupled_Deep_Autoencoder_for_Single_Image_Super-Resolution/links/577619a708aeb9427e275497/Coupled-Deep-Autoencoder-for-Single-Image-Super-Resolution.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/9)

## [Video Super-Resolution With Convolutional Neural Networks](https://ieeexplore.ieee.org/abstract/document/7444187)

[Link do pdf](https://www.qiqindai.com/wp-content/uploads/2018/11/Video-Super-Resolution-With-Convolutional-Neural-Networks.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/10)

## [Computed tomography super-resolution using convolutional neural networks](https://ieeexplore.ieee.org/abstract/document/8297022)

[Link do pdf](https://www.researchgate.net/profile/Zhangyang-Wang/publication/322789361_Computed_tomography_super-resolution_using_convolutional_neural_networks/links/5a6fec3c458515015e61eb0a/Computed-tomography-super-resolution-using-convolutional-neural-networks.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/11)

## [Video Satellite Imagery Super Resolution via Convolutional Neural Networks](https://ieeexplore.ieee.org/abstract/document/8101498)

[Link do pdf](https://www.researchgate.net/profile/Yimin-Luo-3/publication/320954048_Video_Satellite_Imagery_Super_Resolution_via_Convolutional_Neural_Networks/links/5b9a674ba6fdccd3cb5031a2/Video-Satellite-Imagery-Super-Resolution-via-Convolutional-Neural-Networks.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/12)

## [Super-Resolution Using Convolutional Neural Networks Without Any Checkerboard Artifacts](https://ieeexplore.ieee.org/abstract/document/8451141)

[Link do pdf](https://arxiv.org/pdf/1806.02658.pdf)

[Link do issue](https://github.com/ghastcmd/dip/issues/13)