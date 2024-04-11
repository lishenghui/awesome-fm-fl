

Awesome-Foundation-Models-and-Federated-Learning
=================================================

.. raw:: html

   <div align="center">
   <a href="https://arxiv.org/pdf/2406.12844.pdf">
       <img alt="Tests Status" src="https://img.shields.io/badge/arXiv-2406.12844-red?logo=arxiv&style=flat-square&link=https%3A%2F%2Farxiv.org%2Fpdf%2F2206.05359.pdf"/>
   </a>
   <a href="https://arxiv.org/pdf/2406.12844.pdf">
       <img alt="awesome" src="https://awesome.re/badge-flat.svg"/>
   </a>
   <a href="https://github.com/lishenghui/awesome-fm-fl">
       <img alt="Build Status" src="https://img.shields.io/github/last-commit/lishenghui/awesome-fm-fl"/>
   </a>
   <a href="https://github.com/lishenghui/blades/awesome-fm-fl/master/LICENSE">
       <img alt="License" src="https://img.shields.io/github/license/lishenghui/awesome-fm-fl"/>
   </a>
   </div>


This repository is primarily based on our survey paper:


.. raw:: html

   <div align="center">
        <strong><a href="https://arxiv.org/abs/2406.12844">Synergizing Foundation Models and Federated Learning: A Survey</a></strong>
        <div>
            <a href="https://lishenghui.github.io/">Shenghui Li</a>,
            <a href="https://www.fanghuaye.xyz/">Fanghua Ye</a>,
            <a href="https://mengf1.github.io/">Meng Fang</a>,
            <a href="https://scholar.google.com/citations?user=ozQfDTkAAAAJ&hl=en">Jiaxu Zhao</a>,
       </div>
       <div>
           <a href="https://scholar.google.com/citations?hl=en&user=9dJZ9RQAAAAJ">Yun-Hin Chan</a>,
           <a href="https://www.eee.hku.hk/people/echngai/">Edith C.-H. Ngai</a>,
           <a href="https://scholar.google.se/citations?user=xSXvpjEAAAAJ">Thiemo Voigt</a>
        </div>
        <div style="margin-bottom: 20px;"></div>
    </div>


.. raw:: html

   <p align=center>
        <img src="https://github.com/lishenghui/awesome-fm-fl/blob/main/docs/images/fmfltaxonomy.png" width="1000" alt="Taxonomy">
   </p>

|
If you find this survey useful for your research, please consider citing:

::

    @misc{li2024synergizing,
          title={Synergizing Foundation Models and Federated Learning: A Survey},
          author={Shenghui Li and Fanghua Ye and Meng Fang and Jiaxu Zhao and Yun-Hin Chan and Edith C. -H. Ngai and Thiemo Voigt},
          year={2024},
          eprint={2406.12844},
          archivePrefix={arXiv}
    }


.. contents:: Table of Contents
    :depth: 4
    :local:
    :class: collapsible

.. raw:: html

    <script>
    document.addEventListener("DOMContentLoaded", function() {
        var coll = document.getElementsByClassName("collapsible");
        for (var i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.display === "block") {
                    content.style.display = "none";
                } else {
                    content.style.display = "block";
                }
            });
        }
    });
    </script>

Efficiency
###########

Knowledge Distillation 
********************** 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2404.11536">FedPFT: Federated Proxy Fine-Tuning of Foundation Models</a></strong> 
     - IJCAI
     - 2024-08
     - .. image:: https://img.shields.io/github/stars/pzp-dzd/FedPFT 
          :target: https://github.com/pzp-dzd/FedPFT 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29007">FedDAT: An Approach for Foundation Model Finetuning in Multi-Modal Heterogeneous Federated Learning</a></strong> 
     - AAAI
     - 2024-03
     - .. image:: https://img.shields.io/github/stars/HaokunChen245/FedDAT 
          :target: https://github.com/HaokunChen245/FedDAT 
          :alt: GitHub Repo stars
Selective Tuning 
**************** 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2404.11536">FedPFT: Federated Proxy Fine-Tuning of Foundation Models</a></strong> 
     - IJCAI
     - 2024-08
     - .. image:: https://img.shields.io/github/stars/pzp-dzd/FedPFT 
          :target: https://github.com/pzp-dzd/FedPFT 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=TXtRWPZIZ0">FedSelect: Customized Selection of Parameters for Fine-Tuning during Personalized Federated Learning</a></strong> 
     - CVPR
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.1145/3589335.3651931">Only Send What You Need: Learning to Communicate Efficiently in Federated Multilingual Machine Translation</a></strong> 
     - WWW
     - 2024-05
     - -

Additive Tuning
****************

Adapter Tuning 
^^^^^^^^^^^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2404.11536">Federated Adaptation for Foundation Model-based Recommendations</a></strong> 
     - IJCAI
     - 2024-08
     - .. image:: https://img.shields.io/github/stars/Zhangcx19/IJCAI-24-FedPA 
          :target: https://github.com/Zhangcx19/IJCAI-24-FedPA 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10557150">Adapter-based Selective Knowledge Distillation for Federated Multi-domain Meeting Summarization</a></strong> 
     - TASLP
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://danni9594.github.io/publications/CAI24_FedCAF.pdf">Learning Task-Specific Initialization for Effective Federated Continual Fine-Tuning of Foundation Model Adapters</a></strong> 
     - IEEE CAI
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="http://sites.computer.org/debull/A23mar/p52.pdf">FedCLIP: Fast Generalization and Personalization for CLIP in Federated Learning</a></strong> 
     - IEEE DEB
     - 2023-03
     - .. image:: https://img.shields.io/github/stars/microsoft/PersonalizedFL 
          :target: https://github.com/microsoft/PersonalizedFL 
          :alt: GitHub Repo stars

Prompt Tuning
^^^^^^^^^^^^^^

Textual Prompt Tuning 
''''''''''''''''''''' 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.01467">FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models</a></strong> 
     - ICML
     - 2024-07
     - -
   * - .. raw:: html

          <strong><a href="https://openreview.net/pdf?id=bpUgtLeSAp">Personalized Federated Learning for Text Classification with Gradient-Free Prompt Tuning</a></strong> 
     - NAACL
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://aclanthology.org/2023.emnlp-main.488">Federated Learning of Large Language Models with Parameter-Efficient Prompt Tuning and Adaptive Optimization</a></strong> 
     - EMNLP
     - 2023-12
     - .. image:: https://img.shields.io/github/stars/llm-eff/FedPepTAO 
          :target: https://github.com/llm-eff/FedPepTAO 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://aclanthology.org/2023.findings-emnlp.976">Tunable Soft Prompts are Messengers in Federated Learning</a></strong> 
     - EMNLP
     - 2023-12
     - .. image:: https://img.shields.io/github/stars/alibaba/FederatedScope 
          :target: https://github.com/alibaba/FederatedScope/tree/fedsp/federatedscope/nlp/fedsp 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.03123">Efficient Federated Prompt Tuning for Black-box Large Pre-trained Models</a></strong> 
     - arXiv
     - 2023-10
     - -
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10095356">FedPrompt: Communication-Efficient and Privacy-Preserving Prompt Tuning in Federated Learning</a></strong> 
     - ICASSP
     - 2023-05
     - -
Visual Prompt Tuning 
'''''''''''''''''''' 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2310.18285">Unlocking the Potential of Prompt-Tuning in Bridging Generalized and Personalized Federated Learning</a></strong> 
     - CVPR
     - 2024-06
     - .. image:: https://img.shields.io/github/stars/ubc-tea/SGPT 
          :target: https://github.com/ubc-tea/SGPT 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=dUVejidXO7">Visual Prompt Based Personalized Federated Learning</a></strong> 
     - TMLR
     - 2024-02
     - .. image:: https://img.shields.io/github/stars/hkgdifyu/pFedPT 
          :target: https://github.com/hkgdifyu/pFedPT 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10377922">Efficient Model Personalization in Federated Learning via Client-Specific Prompt Generation</a></strong> 
     - ICCV
     - 2023-10
     - -
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10205077">Learning Federated Visual Prompt in Null Space for MRI Reconstruction</a></strong> 
     - CVPR
     - 2023-06
     - .. image:: https://img.shields.io/github/stars/chunmeifeng/FedPR 
          :target: https://github.com/chunmeifeng/FedPR 
          :alt: GitHub Repo stars
Textual-Visual Prompt Tuning 
'''''''''''''''''''''''''''' 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2403.08506">DiPrompT: Disentangled Prompt Tuning for Multiple Latent Domain Generalization in Federated Learning</a></strong> 
     - CVPR
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2403.00041">Global and Local Prompts Cooperation via Optimal Transport for Federated Learning</a></strong> 
     - CVPR
     - 2024-06
     - .. image:: https://img.shields.io/github/stars/HongxiaLee/FedOTP 
          :target: https://github.com/HongxiaLee/FedOTP 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=NW31gAylIm">Federated Text-driven Prompt Generation for Vision-Language Models</a></strong> 
     - ICLR
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29434">Federated Adaptive Prompt Tuning for Multi-Domain Collaborative Learning</a></strong> 
     - AAAI
     - 2024-03
     - .. image:: https://img.shields.io/github/stars/leondada/FedAPT 
          :target: https://github.com/leondada/FedAPT 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2310.03103">Dual Prompt Tuning for Domain-Aware Federated Learning</a></strong> 
     - arXiv
     - 2023-10
     - -
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/abstract/document/10210127">PromptFL: Let Federated Participants Cooperatively Learn Prompts Instead of Models - Federated Learning in Age of Foundation Model</a></strong> 
     - TMC
     - 2023-08
     - -
Reparameterization-Based 
************************ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2406.17706">FedBiOT: LLM Local Fine-tuning in Federated Learning without Full Model</a></strong> 
     - KDD
     - 2024-08
     - .. image:: https://img.shields.io/github/stars/HarliWu/FedBiOT 
          :target: https://github.com/HarliWu/FedBiOT 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=NLPzL6HWNl">Improving LoRA in Privacy-preserving Federated Learning</a></strong> 
     - ICLR
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=JDmAymuFFQ">FL-TAC: Enhanced Fine-Tuning in Federated Learning via Low-Rank</a></strong> 
     - LLMAgents\@ICLR
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.1145/3589335.3651933">FedHLT: Efficient Federated Low-Rank Adaption with Hierarchical Language Tree for Multilingual Modeling</a></strong> 
     - WWW
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2404.15182">FLoRA: Enhancing Vision-Language Models with Parameter-Efficient Federated Learning</a></strong> 
     - arXiv
     - 2024-04
     - -
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10447454">Towards Building The Federatedgpt: Federated Instruction Tuning</a></strong> 
     - ICASSP
     - 2024-03
     - .. image:: https://img.shields.io/github/stars/JayZhang42/FederatedGPT-Shepherd 
          :target: https://github.com/JayZhang42/FederatedGPT-Shepherd 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10447662">Communication-Efficient Personalized Federated Learning for Speech-to-Text Tasks</a></strong> 
     - ICASSP
     - 2024-03
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2403.19211">Dual-Personalizing Adapter for Federated Foundation Models</a></strong> 
     - arXiv
     - 2024-03
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2402.11505">Federated Fine-tuning of Large Language Models under Heterogeneous Language Tasks and Client Resources</a></strong> 
     - arXiv
     - 2024-02
     - .. image:: https://img.shields.io/github/stars/alibaba/FederatedScope 
          :target: https://github.com/alibaba/FederatedScope/tree/FlexLoRA 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2401.06432">Heterogeneous LoRA for Federated Fine-tuning of On-Device Foundation Models</a></strong> 
     - arXiv
     - 2024-01
     - -
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=06quMTmtRV">SLoRA: Federated Parameter Efficient Fine-Tuning of Language Models</a></strong> 
     - FL\@FM-NeurIPS
     - 2023-12
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2312.15926">FedMS: Federated Learning with Mixture of Sparsely Activated Foundations Models</a></strong> 
     - arXiv
     - 2023-12
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2312.17493">Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning</a></strong> 
     - arXiv
     - 2023-12
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2311.11227">FedRA: A Random Allocation Strategy for Federated Tuning to Unleash the Power of Heterogeneous Clients</a></strong> 
     - arXiv
     - 2023-11
     - .. image:: https://img.shields.io/github/stars/leondada/FedRA 
          :target: https://github.com/leondada/FedRA 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2310.13283">pFedLoRA: Model-Heterogeneous Personalized Federated Learning with LoRA Tuning</a></strong> 
     - arXiv
     - 2023-10
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2307.13896">Low-Parameter Federated Learning with Large Language Models</a></strong> 
     - arXiv
     - 2023-07
     - -

Heterogeneous Resource
***********************

Lora 
^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2402.11505">Federated Fine-tuning of Large Language Models under Heterogeneous Language Tasks and Client Resources</a></strong> 
     - arXiv
     - 2024-02
     - .. image:: https://img.shields.io/github/stars/alibaba/FederatedScope 
          :target: https://github.com/alibaba/FederatedScope/tree/FlexLoRA 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2401.06432">Heterogeneous LoRA for Federated Fine-tuning of On-Device Foundation Models</a></strong> 
     - arXiv
     - 2024-01
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2311.11227">FedRA: A Random Allocation Strategy for Federated Tuning to Unleash the Power of Heterogeneous Clients</a></strong> 
     - arXiv
     - 2023-11
     - .. image:: https://img.shields.io/github/stars/leondada/FedRA 
          :target: https://github.com/leondada/FedRA 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2310.13283">pFedLoRA: Model-Heterogeneous Personalized Federated Learning with LoRA Tuning</a></strong> 
     - arXiv
     - 2023-10
     - -
Split Learning 
^^^^^^^^^^^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://icml.cc/virtual/2024/poster/34071">Enhancing Storage and Computational Efficiency in Federated Multimodal Learning for Large-Scale Models</a></strong> 
     - ICML
     - 2024-07
     - .. image:: https://img.shields.io/github/stars/M2FedSA/M-2FedSA 
          :target: https://github.com/M2FedSA/M-2FedSA 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2403.16050">Heterogeneous Federated Learning with Splited Language Model</a></strong> 
     - arXiv
     - 2024-03
     - -
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/9892845">Federated Split BERT for Heterogeneous Text Classification</a></strong> 
     - IJCNN
     - 2022
     - -
Sparsification 
************** 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=06quMTmtRV">SLoRA: Federated Parameter Efficient Fine-Tuning of Language Models</a></strong> 
     - FL\@FM-NeurIPS
     - 2023-12
     - -
Zeroth-Order Optimization 
************************* 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2312.06353">Federated Full-Parameter Tuning of Billion-Sized Language Models with Communication Cost under 18 Kilobytes</a></strong> 
     - ICML
     - 2024-07
     - .. image:: https://img.shields.io/github/stars/alibaba/FederatedScope 
          :target: https://github.com/alibaba/FederatedScope/tree/FedKSeed 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.01467">FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models</a></strong> 
     - ICML
     - 2024-07
     - -
   * - .. raw:: html

          <strong><a href="https://openreview.net/pdf?id=bpUgtLeSAp">Personalized Federated Learning for Text Classification with Gradient-Free Prompt Tuning</a></strong> 
     - NAACL
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2402.05926">On the Convergence of Zeroth-Order Federated Tuning in Large Language Models</a></strong> 
     - arXiv
     - 2024-02
     - .. image:: https://img.shields.io/github/stars/alibaba/FederatedScope 
          :target: https://github.com/alibaba/FederatedScope/tree/FedMeZO 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.05143">ZooPFL: Exploring Black-box Foundation Models for Personalized Federated Learning</a></strong> 
     - arXiv
     - 2023-10
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.03123">Efficient Federated Prompt Tuning for Black-box Large Pre-trained Models</a></strong> 
     - arXiv
     - 2023-10
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2308.13894">FwdLLM: Efficient FedLLM using Forward Gradient</a></strong> 
     - arXiv
     - 2023-08
     - .. image:: https://img.shields.io/github/stars/UbiquitousLearning/FwdLLM 
          :target: https://github.com/UbiquitousLearning/FwdLLM 
          :alt: GitHub Repo stars

Adaptability
#############


Domain-Centric Adaptation
**************************

Multi-Domain Adaptation 
^^^^^^^^^^^^^^^^^^^^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10557150">Adapter-based Selective Knowledge Distillation for Federated Multi-domain Meeting Summarization</a></strong> 
     - TASLP
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2403.08506">DiPrompT: Disentangled Prompt Tuning for Multiple Latent Domain Generalization in Federated Learning</a></strong> 
     - CVPR
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29434">Federated Adaptive Prompt Tuning for Multi-Domain Collaborative Learning</a></strong> 
     - AAAI
     - 2024-03
     - .. image:: https://img.shields.io/github/stars/leondada/FedAPT 
          :target: https://github.com/leondada/FedAPT 
          :alt: GitHub Repo stars
Client-Centric Adaptation 
************************* 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=TXtRWPZIZ0">FedSelect: Customized Selection of Parameters for Fine-Tuning during Personalized Federated Learning</a></strong> 
     - CVPR
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="http://sites.computer.org/debull/A23mar/p52.pdf">FedCLIP: Fast Generalization and Personalization for CLIP in Federated Learning</a></strong> 
     - IEEE DEB
     - 2023-03
     - .. image:: https://img.shields.io/github/stars/microsoft/PersonalizedFL 
          :target: https://github.com/microsoft/PersonalizedFL 
          :alt: GitHub Repo stars

Trustworthiness
################


IP Protection
**************

Black-Box Tuning 
^^^^^^^^^^^^^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.01467">FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models</a></strong> 
     - ICML
     - 2024-07
     - -
   * - .. raw:: html

          <strong><a href="https://openreview.net/pdf?id=bpUgtLeSAp">Personalized Federated Learning for Text Classification with Gradient-Free Prompt Tuning</a></strong> 
     - NAACL
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.05143">ZooPFL: Exploring Black-box Foundation Models for Personalized Federated Learning</a></strong> 
     - arXiv
     - 2023-10
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2310.03123">Efficient Federated Prompt Tuning for Black-box Large Pre-trained Models</a></strong> 
     - arXiv
     - 2023-10
     - -

Privacy Preservation
*********************

Privacy Attack 
^^^^^^^^^^^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://proceedings.mlr.press/v238/vu24a.html"> Analysis of Privacy Leakage in Federated Large Language Models </a></strong> 
     - AISTATS
     - 2024-05
     - .. image:: https://img.shields.io/github/stars/vunhatminh/FL_Attacks 
          :target: https://github.com/vunhatminh/FL_Attacks 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/35b5c175e139bff5f22a5361270fce87-Paper-Conference.pdf">Recovering Private Text in Federated Learning of Language Models</a></strong> 
     - NeurIPS
     - 2022-11
     - .. image:: https://img.shields.io/github/stars/Princeton-SysML/FILM 
          :target: https://github.com/Princeton-SysML/FILM 
          :alt: GitHub Repo stars
Privacy-Preserving Techniques 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=NLPzL6HWNl">Improving LoRA in Privacy-preserving Federated Learning</a></strong> 
     - ICLR
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2312.17493">Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning</a></strong> 
     - arXiv
     - 2023-12
     - -
   * - .. raw:: html

          <strong><a href="https://aclanthology.org/2023.acl-industry.60">Federated Learning of Gboard Language Models with Differential Privacy</a></strong> 
     - ACL
     - 2023-07
     - -

Attack Robustness
******************

Poisoning Attack 
^^^^^^^^^^^^^^^^ 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2406.10630">Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models</a></strong> 
     - arXiv
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://link.springer.com/chapter/10.1007/978-981-97-2259-4_13">Unveiling Backdoor Risks Brought by Foundation Models in Heterogeneous Federated Learning</a></strong> 
     - PAKDD
     - 2024-04
     - .. image:: https://img.shields.io/github/stars/lixi1994/backdoor_FM_hete_FL 
          :target: https://github.com/lixi1994/backdoor_FM_hete_FL 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=BrcHuO2BVc">Backdoor Threats from Compromised Foundation Models to Federated Learning</a></strong> 
     - FL\@FM-NeurIPS
     - 2023-10
     - -

Application
############

Multilingualism 
*************** 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://2024.naacl.org/program/accepted_papers/">Generalizable Multilingual Hate Speech Detection on Low Resource Indian Languages using Fair Selection in Federated Learning</a></strong> 
     - NAACL
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=zzqn5G9fjn">Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages</a></strong> 
     - ICLR
     - 2024-05
     - .. image:: https://img.shields.io/github/stars/Ryan0v0/multilingual_borders 
          :target: https://github.com/Ryan0v0/multilingual_borders 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://doi.org/10.1145/3589335.3651931">Only Send What You Need: Learning to Communicate Efficiently in Federated Multilingual Machine Translation</a></strong> 
     - WWW
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.1145/3589335.3651933">FedHLT: Efficient Federated Low-Rank Adaption with Hierarchical Language Tree for Multilingual Modeling</a></strong> 
     - WWW
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://aclanthology.org/2023.findings-acl.327">Communication Efficient Federated Learning for Multilingual Neural Machine Translation with Adapter</a></strong> 
     - ACL
     - 2023-07
     - .. image:: https://img.shields.io/github/stars/lancopku/FedMNMT 
          :target: https://github.com/lancopku/FedMNMT 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://proceedings.mlr.press/v209/manoel23a.html">Federated Multilingual Models for Medical Transcript Analysis</a></strong> 
     - CHIL
     - 2023-06
     - -
   * - .. raw:: html

          <strong><a href="https://aclanthology.org/2022.naacl-main.101">Pretrained Models for Multilingual Federated Learning</a></strong> 
     - NAACL
     - 2022-07
     - .. image:: https://img.shields.io/github/stars/orionw/Multilingual-Federated-Learning 
          :target: https://github.com/orionw/Multilingual-Federated-Learning 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://doi.org/10.1145/3485447.3511988">FedKC: Federated Knowledge Composition for Multilingual Natural Language Understanding</a></strong> 
     - WWW
     - 2022-04
     - -
Speech 
****** 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10447662">Communication-Efficient Personalized Federated Learning for Speech-to-Text Tasks</a></strong> 
     - ICASSP
     - 2024-03
     - -
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10389738">Joint Federated Learning and Personalization for on-Device ASR</a></strong> 
     - ASRU
     - 2023-12
     - -
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10389620">Importance of Smoothness Induced by Optimizers in Fl4Asr: Towards Understanding Federated Learning for End-To-End ASR</a></strong> 
     - ASRU
     - 2023-12
     - -
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=ozN92d7CHX">Federated Learning for Speech Recognition: Revisiting Current Trends Towards Large-Scale ASR</a></strong> 
     - FL\@FM-NeurIPS
     - 2023-12
     - -
Recommendation Systems 
********************** 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2404.11536">Federated Adaptation for Foundation Model-based Recommendations</a></strong> 
     - IJCAI
     - 2024-08
     - .. image:: https://img.shields.io/github/stars/Zhangcx19/IJCAI-24-FedPA 
          :target: https://github.com/Zhangcx19/IJCAI-24-FedPA 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2406.00004">Navigating the Future of Federated Recommendation Systems with Foundation Models</a></strong> 
     - arXiv
     - 2024-06
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.1145/3589334.3645337">Prompt-enhanced Federated Content Representation Learning for Cross-domain Recommendation</a></strong> 
     - WWW
     - 2024-05
     - .. image:: https://img.shields.io/github/stars/Ckano/PFCR 
          :target: https://github.com/Ckano/PFCR 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2403.04256">Federated Recommendation via Hybrid Retrieval Augmented Generation</a></strong> 
     - arXiv
     - 2024-03
     - .. image:: https://img.shields.io/github/stars/huiminzeng/GPT-FedRec 
          :target: https://github.com/huiminzeng/GPT-FedRec 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2402.09959">LLM-based Federated Recommendation</a></strong> 
     - arXiv
     - 2024-02
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2402.01124">TransFR: Transferable Federated Recommendation with Pre-trained Language Models</a></strong> 
     - arXiv
     - 2024-02
     - -
Domain Specific 
*************** 


.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2404.11536">Federated Prompt Learning for Weather Foundation Models on Devices</a></strong> 
     - IJCAI
     - 2024-08
     - .. image:: https://img.shields.io/github/stars/shengchaochen82/FedPoD 
          :target: https://github.com/shengchaochen82/FedPoD 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://link.springer.com/article/10.1007/s11280-024-01266-3">Foundation models matter: federated learning for multi-center tuberculosis diagnosis via adaptive regularization and model-contrastive learning</a></strong> 
     - WWW
     - 2024-05
     - -
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2403.05408">FedFMS: Exploring Federated Foundation Models for Medical Image Segmentation</a></strong> 
     - MICCAI
     - 2024
     - .. image:: https://img.shields.io/github/stars/LIU-YUXI/FedFMS 
          :target: https://github.com/LIU-YUXI/FedFMS 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://doi.org/10.24963/ijcai.2023/393">Prompt Federated Learning for Weather Forecasting: Toward Foundation Models on Meteorological Data</a></strong> 
     - IJCAI
     - 2023-8
     - -
   * - .. raw:: html

          <strong><a href="https://aclanthology.org/2023.emnlp-main.734">FedTherapist: Mental Health Monitoring with User-Generated Linguistic Expressions on Smartphones via Federated Learning</a></strong> 
     - EMNLP
     - 2023-12
     - -
   * - .. raw:: html

          <strong><a href="https://doi.org/10.48550/arXiv.2309.08173">FedJudge: Federated Legal Large Language Model</a></strong> 
     - arXiv
     - 2023-09
     - .. image:: https://img.shields.io/github/stars/yuelinan/FedJudge 
          :target: https://github.com/yuelinan/FedJudge 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://aclanthology.org/2023.acl-long.193">FEDLEGAL: The First Real-World Federated Learning Benchmark for Legal NLP</a></strong> 
     - ACL
     - 2023-07
     - .. image:: https://img.shields.io/github/stars/SMILELab-FL/FedLegal 
          :target: https://github.com/SMILELab-FL/FedLegal 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/document/10205077">Learning Federated Visual Prompt in Null Space for MRI Reconstruction</a></strong> 
     - CVPR
     - 2023-06
     - .. image:: https://img.shields.io/github/stars/chunmeifeng/FedPR 
          :target: https://github.com/chunmeifeng/FedPR 
          :alt: GitHub Repo stars
   * - .. raw:: html

          <strong><a href="https://proceedings.mlr.press/v209/manoel23a.html">Federated Multilingual Models for Medical Transcript Analysis</a></strong> 
     - CHIL
     - 2023-06
     - -

Resources
##########

Frameworks 
********** 


.. list-table::
   :widths: 40 10 10 20 20
   :header-rows: 1

   * - Title
     - Venue
     - Year
     - GitHub
     - Developed by
   * - .. raw:: html

          <strong><a href="http://jmlr.org/papers/v24/22-0440.html">FedLab: A Flexible Federated Learning Framework</a></strong> 
     - JMLR
     - 2023
     - .. image:: https://img.shields.io/github/stars/SMILELab-FL/FedLab 
          :target: https://github.com/SMILELab-FL/FedLab 
          :alt: GitHub Repo stars
     - SMILELab
   * - .. raw:: html

          <strong><a href="https://www.vldb.org/pvldb/vol16/p1059-li.pdf">FederatedScope: A Flexible Federated Learning Platform for Heterogeneity</a></strong> 
     - VLDB
     - 2023
     - .. image:: https://img.shields.io/github/stars/alibaba/FederatedScope 
          :target: https://github.com/alibaba/FederatedScope 
          :alt: GitHub Repo stars
     - .. raw:: html

          <img src="https://img.shields.io/badge/Alibaba-white?logo=alibabadotcom" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/>
   * - .. raw:: html

          <strong><a href="https://proceedings.mlr.press/v162/lai22a.html">FedScale: Benchmarking Model and System Performance of Federated Learning at Scale</a></strong> 
     - ICML
     - 2022-07
     - .. image:: https://img.shields.io/github/stars/SymbioticLab/FedScale 
          :target: https://github.com/SymbioticLab/FedScale 
          :alt: GitHub Repo stars
     - Umich
   * - .. raw:: html

          <strong><a href="https://openreview.net/forum?id=hD9QaIQTL_f">NVIDIA FLARE: Federated Learning from Simulation to Real-World</a></strong> 
     - FL\@NeurIPS
     - 2022
     - .. image:: https://img.shields.io/github/stars/NVIDIA/NVFlare 
          :target: https://github.com/NVIDIA/NVFlare 
          :alt: GitHub Repo stars
     - .. raw:: html

          <img src="https://img.shields.io/badge/Nvidia-white?logo=nvidia" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/>
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2203.13789">FLUTE: A Scalable Extensible Framework for High-Performance Federated Learning Simulations</a></strong> 
     - FL\@NeurIPS
     - 2022
     - .. image:: https://img.shields.io/github/stars/microsoft/msrflute 
          :target: https://github.com/microsoft/msrflute 
          :alt: GitHub Repo stars
     - Microsoft
   * - .. raw:: html

          <strong><a href="https://ieeexplore.ieee.org/abstract/document/9826069">Scalable federated machine learning with FEDn</a></strong> 
     - CCGrid
     - 2022
     - .. image:: https://img.shields.io/github/stars/scaleoutsystems/fedn 
          :target: https://github.com/scaleoutsystems/fedn 
          :alt: GitHub Repo stars
     - Scaleout
   * - .. raw:: html

          <strong><a href="http://jmlr.org/papers/v22/20-815.html">FATE: An Industrial Grade Platform for Collaborative Learning With Data Protection</a></strong> 
     - JMLR
     - 2021
     - .. image:: https://img.shields.io/github/stars/FederatedAI/FATE 
          :target: https://github.com/FederatedAI/FATE 
          :alt: GitHub Repo stars
     - Webank
   * - .. raw:: html

          <strong><a href="https://flower.ai/">Flower: A friendly federated learning research framework</a></strong> 
     - Arxiv
     - 2020
     - .. image:: https://img.shields.io/github/stars/adap/flower 
          :target: https://github.com/adap/flower 
          :alt: GitHub Repo stars
     - Flower Labs
   * - .. raw:: html

          <strong><a href="https://arxiv.org/abs/2007.13518">FedML: A Research Library and Benchmark for Federated Machine Learning</a></strong> 
     - SpicyFL
     - 2020
     - .. image:: https://img.shields.io/github/stars/FedML-AI/FedML 
          :target: https://github.com/FedML-AI/FedML 
          :alt: GitHub Repo stars
     - FedML


