# 😎Awesome Foundation Models and Federated Learning

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

This repository is primarily based on our survey paper 📚🔍:

<div align="center">
     <strong><a href="https://arxiv.org/abs/2406.12844"> Synergizing Foundation Models and Federated Learning: A Survey </a></strong>
     <div>
         <a href="https://lishenghui.github.io/">Shenghui Li,</a>
         <a href="https://www.fanghuaye.xyz/">Fanghua Ye,</a>
         <a href="https://mengf1.github.io/">Meng Fang,</a>
         <a href="https://scholar.google.com/citations?user=ozQfDTkAAAAJ&hl=en">Jiaxu Zhao,</a>
        <a href="https://scholar.google.com/citations?hl=en&user=9dJZ9RQAAAAJ">Yun-Hin Chan,</a>
        <a href="https://www.eee.hku.hk/people/echngai/">Edith C. H. Ngai,</a>
        <a href="https://scholar.google.se/citations?user=xSXvpjEAAAAJ">Thiemo Voigt</a>
     </div>
     <div align="left">
         Unlike smaller models, Foundation Models (FMs), such as LLMs and VLMs, are built upon vast amounts of training data 📊. While general FMs can use public data, domain-specific FMs require proprietary data for pre-training and fine-tuning, raising privacy concerns 🔒. Federated Learning (FL) 🤝💻, a compelling privacy-preserving approach, enables collaborative learning across distributed datasets while maintaining data privacy🛡️. Synergizing FM and FL offers a promising way to address data availability and privacy challenges in FM development, potentially revolutionizing large-scale machine learning in sensitive domains. 
     </div>
     <div style="margin-bottom: 10px;"></div>
 </div>

---

<p align=center>
     <img src="https://github.com/lishenghui/awesome-fm-fl/blob/main/docs/images/fmfltaxonomy.png" width="1000" alt="Taxonomy">
</p>

---

🙏If you find this survey useful for your research, please consider citing:

    @misc{li2024synergizing,
          title={Synergizing Foundation Models and Federated Learning: A Survey},
          author={Shenghui Li and Fanghua Ye and Meng Fang and Jiaxu Zhao and Yun-Hin Chan and Edith C. -H. Ngai and Thiemo Voigt},
          year={2024},
          eprint={2406.12844},
          archivePrefix={arXiv}
    }

<div class="contents collapsible" depth="3" local="">
<strong>Table of Contents</strong>
<ul>
<li><details open><summary><a href="#efficiency">Efficiency</a></summary><ul>
<li><details><summary><a href="#parameter-efficient-fine-tuning">Parameter-Efficient Fine-Tuning</a></summary><ul>
<li><a href="#selective-tuning-7">Selective Tuning (7)</a></li>
<li><details><summary><a href="#additive-tuning">Additive Tuning</a></summary><ul>
<li><a href="#adapter-tuning-10">Adapter Tuning (10)</a></li>
<li><a href="#prompt-tuning-19">Prompt Tuning (19)</a></li>
</ul></details></li>
<li><a href="#reparameterization-based-32">Reparameterization-Based (32)</a></li>
</ul></details></li>
<li><details><summary><a href="#model-compression">Model Compression</a></summary><ul>
<li><a href="#knowledge-distillation-10">Knowledge Distillation (10)</a></li>
<li><a href="#sparsification-15">Sparsification (15)</a></li>
<li><a href="#quantization-3">Quantization (3)</a></li>
</ul></details></li>
<li><details><summary><a href="#heterogeneous-resource">Heterogeneous Resource</a></summary><ul>
<li><a href="#lora-31">Lora (31)</a></li>
<li><a href="#split-learning-9">Split Learning (9)</a></li>
</ul></details></li>
<li><a href="#zeroth-order-optimization-9">Zeroth-Order Optimization (9)</a></li>
</ul></details></li>
<li><details open><summary><a href="#adaptability">Adaptability</a></summary><ul>
<li><details><summary><a href="#domain-centric-adaptation">Domain-Centric Adaptation</a></summary><ul>
<li><a href="#multi-domain-adaptation-7">Multi-Domain Adaptation (7)</a></li>
</ul></details></li>
<li><details><summary><a href="#client-centric-adaptation">Client-Centric Adaptation</a></summary><ul>
<li><a href="#preference-aware-adaptation-3">Preference-Aware Adaptation (3)</a></li>
<li><a href="#personalization-9">Personalization (9)</a></li>
<li><a href="#clustering-4">Clustering (4)</a></li>
</ul></details></li>
</ul></details></li>
<li><details open><summary><a href="#trustworthiness">Trustworthiness</a></summary><ul>
<li><details><summary><a href="#ip-protection">IP Protection</a></summary><ul>
<li><a href="#black-box-tuning-4">Black-Box Tuning (4)</a></li>
</ul></details></li>
<li><details><summary><a href="#privacy-preservation">Privacy Preservation</a></summary><ul>
<li><a href="#privacy-attack-6">Privacy Attack (6)</a></li>
<li><a href="#privacy-preserving-techniques-8">Privacy-Preserving Techniques (8)</a></li>
</ul></details></li>
<li><details><summary><a href="#attack-robustness">Attack Robustness</a></summary><ul>
<li><a href="#poisoning-attack-8">Poisoning Attack (8)</a></li>
</ul></details></li>
</ul></details></li>
<li><details open><summary><a href="#application">Application</a></summary><ul>
<li><a href="#multilingualism-9">Multilingualism (9)</a></li>
<li><a href="#speech-4">Speech (4)</a></li>
<li><a href="#recommendation-systems-7">Recommendation Systems (7)</a></li>
<li><a href="#domain-specific-11">Domain Specific (11)</a></li>
</ul></details></li>
<li><details open><summary><a href="#resources">Resources</a></summary><ul>
<li><a href="#surveys-11">Surveys (11)</a></li>
<li><a href="#frameworks-11">Frameworks (11)</a></li>
</ul></details></li>
</ul>
</div>

## Efficiency

### Parameter-Efficient Fine-Tuning

#### Selective Tuning (7)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2510.04601">FedSRD: Sparsify-Reconstruct-Decompose for Communication-Efficient Federated Large Language Models Fine-Tuning</a></strong> </td>
<td>arXiv</td>
<td>2025-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2411.11912">F\textasciicircum3OCUS - Federated Finetuning of Vision-Language Foundation Models with Optimal Client Layer Updating Strategy via Multi-objective Meta-Heuristics</a></strong> </td>
<td>CVPR</td>
<td>2025-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2503.10217">Efficient Federated Fine-Tuning of Large Language Models with Layer Dropout</a></strong> </td>
<td>arXiv</td>
<td>2025-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2404.11536">FedPFT: Federated Proxy Fine-Tuning of Foundation Models</a></strong> </td>
<td>IJCAI</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/pzp-dzd/FedPFT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=TXtRWPZIZ0">FedSelect: Customized Selection of Parameters for Fine-Tuning during Personalized Federated Learning</a></strong> </td>
<td>CVPR</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2406.05233">Federated LoRA with Sparse Communication</a></strong> </td>
<td>arXiv</td>
<td>2024-06</td>
<td><img src="https://img.shields.io/github/stars/imkevinkuo/flasc" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.1145/3589335.3651931">Only Send What You Need: Learning to Communicate Efficiently in Federated Multilingual Machine Translation</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

#### Additive Tuning

##### Adapter Tuning (10)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2025.findings-acl.1241/">Communication-Efficient and Tensorized Federated Fine-Tuning of Large Language Models</a></strong> </td>
<td>ACL</td>
<td>2025-07</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=3wEGdrV5Cb">Enhancing Federated Domain Adaptation with Multi-Domain Prototype-Based Federated Fine-Tuning</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf">DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting</a></strong> </td>
<td>NeurIPS</td>
<td>2024-09</td>
<td><img src="https://img.shields.io/github/stars/1xbq1/DoFIT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2404.11536">Federated Adaptation for Foundation Model-based Recommendations</a></strong> </td>
<td>IJCAI</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/Zhangcx19/IJCAI-24-FedPA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10557150">Adapter-based Selective Knowledge Distillation for Federated Multi-domain Meeting Summarization</a></strong> </td>
<td>TASLP</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://danni9594.github.io/publications/CAI24_FedCAF.pdf">Learning Task-Specific Initialization for Effective Federated Continual Fine-Tuning of Foundation Model Adapters</a></strong> </td>
<td>IEEE CAI</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29007">FedDAT: An Approach for Foundation Model Finetuning in Multi-Modal Heterogeneous Federated Learning</a></strong> </td>
<td>AAAI</td>
<td>2024-03</td>
<td><img src="https://img.shields.io/github/stars/HaokunChen245/FedDAT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10389738">Joint Federated Learning and Personalization for on-Device ASR</a></strong> </td>
<td>ASRU</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2023.findings-acl.327">Communication Efficient Federated Learning for Multilingual Neural Machine Translation with Adapter</a></strong> </td>
<td>ACL</td>
<td>2023-07</td>
<td><img src="https://img.shields.io/github/stars/lancopku/FedMNMT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="http://sites.computer.org/debull/A23mar/p52.pdf">FedCLIP: Fast Generalization and Personalization for CLIP in Federated Learning</a></strong> </td>
<td>IEEE DEB</td>
<td>2023-03</td>
<td><img src="https://img.shields.io/github/stars/microsoft/PersonalizedFL" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
</tbody>
</table>

##### Prompt Tuning (19)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=xiDJaTim3P">Mixture of Experts Made Personalized: Federated Prompt Learning for Vision-Language Models</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=Equ277PBN0">Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.01467">FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models</a></strong> </td>
<td>ICML</td>
<td>2024-07</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2024.findings-naacl.286.pdf">Personalized Federated Learning for Text Classification with Gradient-Free Prompt Tuning</a></strong> </td>
<td>NAACL</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2403.08506">DiPrompT: Disentangled Prompt Tuning for Multiple Latent Domain Generalization in Federated Learning</a></strong> </td>
<td>CVPR</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2310.18285">Unlocking the Potential of Prompt-Tuning in Bridging Generalized and Personalized Federated Learning</a></strong> </td>
<td>CVPR</td>
<td>2024-06</td>
<td><img src="https://img.shields.io/github/stars/ubc-tea/SGPT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2403.00041">Global and Local Prompts Cooperation via Optimal Transport for Federated Learning</a></strong> </td>
<td>CVPR</td>
<td>2024-06</td>
<td><img src="https://img.shields.io/github/stars/HongxiaLee/FedOTP" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=NW31gAylIm">Federated Text-driven Prompt Generation for Vision-Language Models</a></strong> </td>
<td>ICLR</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29434">Federated Adaptive Prompt Tuning for Multi-Domain Collaborative Learning</a></strong> </td>
<td>AAAI</td>
<td>2024-03</td>
<td><img src="https://img.shields.io/github/stars/leondada/FedAPT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=dUVejidXO7">Visual Prompt Based Personalized Federated Learning</a></strong> </td>
<td>TMLR</td>
<td>2024-02</td>
<td><img src="https://img.shields.io/github/stars/hkgdifyu/pFedPT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2023.emnlp-main.488">Federated Learning of Large Language Models with Parameter-Efficient Prompt Tuning and Adaptive Optimization</a></strong> </td>
<td>EMNLP</td>
<td>2023-12</td>
<td><img src="https://img.shields.io/github/stars/llm-eff/FedPepTAO" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2023.findings-emnlp.976">Tunable Soft Prompts are Messengers in Federated Learning</a></strong> </td>
<td>EMNLP</td>
<td>2023-12</td>
<td><img src="https://img.shields.io/github/stars/alibaba/FederatedScope" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.03123">Efficient Federated Prompt Tuning for Black-box Large Pre-trained Models</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10377922">Efficient Model Personalization in Federated Learning via Client-Specific Prompt Generation</a></strong> </td>
<td>ICCV</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2310.03103">Dual Prompt Tuning for Domain-Aware Federated Learning</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10210127">PromptFL: Let Federated Participants Cooperatively Learn Prompts Instead of Models - Federated Learning in Age of Foundation Model</a></strong> </td>
<td>TMC</td>
<td>2023-08</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10205077">Learning Federated Visual Prompt in Null Space for MRI Reconstruction</a></strong> </td>
<td>CVPR</td>
<td>2023-06</td>
<td><img src="https://img.shields.io/github/stars/chunmeifeng/FedPR" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10095356">FedPrompt: Communication-Efficient and Privacy-Preserving Prompt Tuning in Federated Learning</a></strong> </td>
<td>ICASSP</td>
<td>2023-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.1145/3543507.3583518">pFedPrompt: Learning Personalized Prompt for Vision-Language Models in Federated Learning</a></strong> </td>
<td>WWW</td>
<td>2023-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

#### Reparameterization-Based (32)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2510.04601">FedSRD: Sparsify-Reconstruct-Decompose for Communication-Efficient Federated Large Language Models Fine-Tuning</a></strong> </td>
<td>arXiv</td>
<td>2025-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2509.01750">Communication-Aware Knowledge Distillation for Federated LLM Fine-Tuning over Wireless Networks</a></strong> </td>
<td>arXiv</td>
<td>2025-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2504.16023">PointLoRA: Low-Rank Adaptation with Token Selection for Point Cloud Learning</a></strong> </td>
<td>CVPR</td>
<td>2025-06</td>
<td><img src="https://img.shields.io/github/stars/songw-zju/PointLoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/11044514">FLM-TopK: Expediting Federated Large Language Model Tuning by Sparsifying Intervalized Gradients</a></strong> </td>
<td>INFOCOM</td>
<td>2025-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/11044641">Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA</a></strong> </td>
<td>INFOCOM</td>
<td>2025-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=iX3uESGdsO">Selective Aggregation for Low-Rank Adaptation in Federated Learning</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/Pengxin-Guo/FedSA-LoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=ROpY0qRUXL">Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=e0rQRMUhs7">Federated Residual Low-Rank Adaption of Large Language Models</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/IAMJackYan/FRLoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10855336">Federated Fine-Tuning for Pre-Trained Foundation Models Over Wireless Networks</a></strong> </td>
<td>IEEE TWC</td>
<td>2025-01</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10666083">FedFMSL: Federated Learning of Foundation Models With Sparsely Activated LoRA</a></strong> </td>
<td>IEEE TMC</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10818586">Data Reconstruction and Protection in Federated Learning for Fine-Tuning Large Language Models</a></strong> </td>
<td>IEEE TBD</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2024.emnlp-main.717">Heterogeneous LoRA for Federated Fine-tuning of On-Device Foundation Models</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.findings-emnlp.615/">Promoting Data and Model Privacy in Federated Learning through Quantized LoRA</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2411.19128">Personalized Federated Fine-Tuning for LLMs via Data-Driven Heterogeneous Model Architectures</a></strong> </td>
<td>arXiv</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2311.11227">FedRA: A Random Allocation Strategy for Federated Tuning to Unleash the Power of Heterogeneous Clients</a></strong> </td>
<td>ECCV</td>
<td>2024-10</td>
<td><img src="https://img.shields.io/github/stars/leondada/FedRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2410.10200">Fed-piLot: Optimizing LoRA Assignment for Efficient Federated Foundation Model Fine-Tuning</a></strong> </td>
<td>arXiv</td>
<td>2024-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=gkOzoHBXUw">Federated Fine-tuning of Large Language Models under Heterogeneous Language Tasks and Client Resources</a></strong> </td>
<td>NeurIPS</td>
<td>2024-09</td>
<td><img src="https://img.shields.io/github/stars/alibaba/FederatedScope" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=nkwPiBSw1f">Dual-Personalizing Adapter for Federated Foundation Models</a></strong> </td>
<td>NeurIPS</td>
<td>2024-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://dl.acm.org/doi/abs/10.1145/3682068">Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning</a></strong> </td>
<td>ACM TMIS</td>
<td>2024-08</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://dl.acm.org/doi/abs/10.1145/3637528.3671897">FedBiOT: LLM Local Fine-tuning in Federated Learning without Full Model</a></strong> </td>
<td>KDD</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/HarliWu/FedBiOT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2406.05233">Federated LoRA with Sparse Communication</a></strong> </td>
<td>arXiv</td>
<td>2024-06</td>
<td><img src="https://img.shields.io/github/stars/imkevinkuo/flasc" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2024.findings-naacl.98">FedLFC: Towards Efficient Federated Multilingual Modeling with LoRA-based Language Family Clustering</a></strong> </td>
<td>NAACL</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=NLPzL6HWNl">Improving LoRA in Privacy-preserving Federated Learning</a></strong> </td>
<td>ICLR</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.1145/3589335.3651933">FedHLT: Efficient Federated Low-Rank Adaption with Hierarchical Language Tree for Multilingual Modeling</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=JDmAymuFFQ">FL-TAC: Enhanced Fine-Tuning in Federated Learning via Low-Rank, Task-Specific Adapter Clustering</a></strong> </td>
<td>LLMAgents@ICLR</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2404.15182">FLoRA: Enhancing Vision-Language Models with Parameter-Efficient Federated Learning</a></strong> </td>
<td>arXiv</td>
<td>2024-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10447454">Towards Building The Federatedgpt: Federated Instruction Tuning</a></strong> </td>
<td>ICASSP</td>
<td>2024-03</td>
<td><img src="https://img.shields.io/github/stars/JayZhang42/FederatedGPT-Shepherd" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10447662">Communication-Efficient Personalized Federated Learning for Speech-to-Text Tasks</a></strong> </td>
<td>ICASSP</td>
<td>2024-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2403.06131">FedPIT: Towards Privacy-preserving and Few-shot Federated Instruction Tuning</a></strong> </td>
<td>arXiv</td>
<td>2024-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=06quMTmtRV">SLoRA: Federated Parameter Efficient Fine-Tuning of Language Models</a></strong> </td>
<td>FL@FM-NeurIPS</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2310.13283">pFedLoRA: Model-Heterogeneous Personalized Federated Learning with LoRA Tuning</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2307.13896">Low-Parameter Federated Learning with Large Language Models</a></strong> </td>
<td>arXiv</td>
<td>2023-07</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Model Compression

#### Knowledge Distillation (10)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2025.findings-emnlp.454/">FedCoT: Federated Chain-of-Thought Distillation for Large Language Models</a></strong> </td>
<td>EMNLP</td>
<td>2025-11</td>
<td><img src="https://img.shields.io/github/stars/FederatedAI/FATE-LLM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2025.emnlp-main.747/">PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation</a></strong> </td>
<td>EMNLP</td>
<td>2025-11</td>
<td><img src="https://img.shields.io/github/stars/FederatedAI/FATE-LLM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2509.01750">Communication-Aware Knowledge Distillation for Federated LLM Fine-Tuning over Wireless Networks</a></strong> </td>
<td>arXiv</td>
<td>2025-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/11180881">Federated Fine-Tuning of LLMs: Framework Comparison and Research Directions</a></strong> </td>
<td>IEEE Commun. Mag.</td>
<td>2025-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.1145/3742788">Grounding Foundation Models through Federated Transfer Learning: A General Framework</a></strong> </td>
<td>ACM TIST</td>
<td>2025-08</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2025.coling-main.17.pdf">FedMKT: Federated Mutual Knowledge Transfer for Large and Small Language Models</a></strong> </td>
<td>ACL</td>
<td>2025-01</td>
<td><img src="https://img.shields.io/github/stars/FederatedAI/FATE-LLM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2404.11536">FedPFT: Federated Proxy Fine-Tuning of Foundation Models</a></strong> </td>
<td>IJCAI</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/pzp-dzd/FedPFT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10557150">Adapter-based Selective Knowledge Distillation for Federated Multi-domain Meeting Summarization</a></strong> </td>
<td>TASLP</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2405.14212">Federated Domain-Specific Knowledge Transfer on Large Language Models Using Synthetic Data</a></strong> </td>
<td>arXiv</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29007">FedDAT: An Approach for Foundation Model Finetuning in Multi-Modal Heterogeneous Federated Learning</a></strong> </td>
<td>AAAI</td>
<td>2024-03</td>
<td><img src="https://img.shields.io/github/stars/HaokunChen245/FedDAT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
</tbody>
</table>

#### Sparsification (15)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2508.19078">Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices</a></strong> </td>
<td>Eurosys</td>
<td>2026-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2025.emnlp-main.747/">PPC-GPT: Federated Task-Specific Compression of Large Language Models via Pruning and Chain-of-Thought Distillation</a></strong> </td>
<td>EMNLP</td>
<td>2025-11</td>
<td><img src="https://img.shields.io/github/stars/FederatedAI/FATE-LLM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2510.04601">FedSRD: Sparsify-Reconstruct-Decompose for Communication-Efficient Federated Large Language Models Fine-Tuning</a></strong> </td>
<td>arXiv</td>
<td>2025-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html">FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation</a></strong> </td>
<td>ICCV</td>
<td>2025-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2508.17209">Memory-Efficient Federated Fine-Tuning of Large Language Models via Layer Pruning</a></strong> </td>
<td>arXiv</td>
<td>2025-08</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2504.16023">PointLoRA: Low-Rank Adaptation with Token Selection for Point Cloud Learning</a></strong> </td>
<td>CVPR</td>
<td>2025-06</td>
<td><img src="https://img.shields.io/github/stars/songw-zju/PointLoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/11044514">FLM-TopK: Expediting Federated Large Language Model Tuning by Sparsifying Intervalized Gradients</a></strong> </td>
<td>INFOCOM</td>
<td>2025-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2025.naacl-long.424/">FedSpaLLM: Federated Pruning of Large Language Models</a></strong> </td>
<td>NAACL</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/BaiTheBest/FedSpaLLM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10666083">FedFMSL: Federated Learning of Foundation Models With Sparsely Activated LoRA</a></strong> </td>
<td>IEEE TMC</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10818586">Data Reconstruction and Protection in Federated Learning for Fine-Tuning Large Language Models</a></strong> </td>
<td>IEEE TBD</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.findings-emnlp.615/">Promoting Data and Model Privacy in Federated Learning through Quantized LoRA</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2406.05233">Federated LoRA with Sparse Communication</a></strong> </td>
<td>arXiv</td>
<td>2024-06</td>
<td><img src="https://img.shields.io/github/stars/imkevinkuo/flasc" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2406.11187">Save It All: Enabling Full Parameter Tuning for Federated Large Language Models via Cycle Block Gradient Descent</a></strong> </td>
<td>arXiv</td>
<td>2024-06</td>
<td><img src="https://img.shields.io/github/stars/L3030/FedCyBGD" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.1145/3589335.3651931">Only Send What You Need: Learning to Communicate Efficiently in Federated Multilingual Machine Translation</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=06quMTmtRV">SLoRA: Federated Parameter Efficient Fine-Tuning of Language Models</a></strong> </td>
<td>FL@FM-NeurIPS</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

#### Quantization (3)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/11044514">FLM-TopK: Expediting Federated Large Language Model Tuning by Sparsifying Intervalized Gradients</a></strong> </td>
<td>INFOCOM</td>
<td>2025-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/11044641">Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA</a></strong> </td>
<td>INFOCOM</td>
<td>2025-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.findings-emnlp.615/">Promoting Data and Model Privacy in Federated Learning through Quantized LoRA</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Heterogeneous Resource

#### Lora (31)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2510.04601">FedSRD: Sparsify-Reconstruct-Decompose for Communication-Efficient Federated Large Language Models Fine-Tuning</a></strong> </td>
<td>arXiv</td>
<td>2025-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2509.01750">Communication-Aware Knowledge Distillation for Federated LLM Fine-Tuning over Wireless Networks</a></strong> </td>
<td>arXiv</td>
<td>2025-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2504.16023">PointLoRA: Low-Rank Adaptation with Token Selection for Point Cloud Learning</a></strong> </td>
<td>CVPR</td>
<td>2025-06</td>
<td><img src="https://img.shields.io/github/stars/songw-zju/PointLoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/11044514">FLM-TopK: Expediting Federated Large Language Model Tuning by Sparsifying Intervalized Gradients</a></strong> </td>
<td>INFOCOM</td>
<td>2025-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/11044641">Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA</a></strong> </td>
<td>INFOCOM</td>
<td>2025-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=iX3uESGdsO">Selective Aggregation for Low-Rank Adaptation in Federated Learning</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/Pengxin-Guo/FedSA-LoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=ROpY0qRUXL">Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=e0rQRMUhs7">Federated Residual Low-Rank Adaption of Large Language Models</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/IAMJackYan/FRLoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10855336">Federated Fine-Tuning for Pre-Trained Foundation Models Over Wireless Networks</a></strong> </td>
<td>IEEE TWC</td>
<td>2025-01</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10666083">FedFMSL: Federated Learning of Foundation Models With Sparsely Activated LoRA</a></strong> </td>
<td>IEEE TMC</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10818586">Data Reconstruction and Protection in Federated Learning for Fine-Tuning Large Language Models</a></strong> </td>
<td>IEEE TBD</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2024.emnlp-main.717">Heterogeneous LoRA for Federated Fine-tuning of On-Device Foundation Models</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.findings-emnlp.615/">Promoting Data and Model Privacy in Federated Learning through Quantized LoRA</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2411.19128">Personalized Federated Fine-Tuning for LLMs via Data-Driven Heterogeneous Model Architectures</a></strong> </td>
<td>arXiv</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2311.11227">FedRA: A Random Allocation Strategy for Federated Tuning to Unleash the Power of Heterogeneous Clients</a></strong> </td>
<td>ECCV</td>
<td>2024-10</td>
<td><img src="https://img.shields.io/github/stars/leondada/FedRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2410.10200">Fed-piLot: Optimizing LoRA Assignment for Efficient Federated Foundation Model Fine-Tuning</a></strong> </td>
<td>arXiv</td>
<td>2024-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=gkOzoHBXUw">Federated Fine-tuning of Large Language Models under Heterogeneous Language Tasks and Client Resources</a></strong> </td>
<td>NeurIPS</td>
<td>2024-09</td>
<td><img src="https://img.shields.io/github/stars/alibaba/FederatedScope" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://dl.acm.org/doi/abs/10.1145/3682068">Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning</a></strong> </td>
<td>ACM TMIS</td>
<td>2024-08</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://dl.acm.org/doi/abs/10.1145/3637528.3671897">FedBiOT: LLM Local Fine-tuning in Federated Learning without Full Model</a></strong> </td>
<td>KDD</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/HarliWu/FedBiOT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2406.05233">Federated LoRA with Sparse Communication</a></strong> </td>
<td>arXiv</td>
<td>2024-06</td>
<td><img src="https://img.shields.io/github/stars/imkevinkuo/flasc" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.findings-naacl.98">FedLFC: Towards Efficient Federated Multilingual Modeling with LoRA-based Language Family Clustering</a></strong> </td>
<td>NAACL</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=NLPzL6HWNl">Improving LoRA in Privacy-preserving Federated Learning</a></strong> </td>
<td>ICLR</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.1145/3589335.3651933">FedHLT: Efficient Federated Low-Rank Adaption with Hierarchical Language Tree for Multilingual Modeling</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=JDmAymuFFQ">FL-TAC: Enhanced Fine-Tuning in Federated Learning via Low-Rank, Task-Specific Adapter Clustering</a></strong> </td>
<td>LLMAgents@ICLR</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2404.15182">FLoRA: Enhancing Vision-Language Models with Parameter-Efficient Federated Learning</a></strong> </td>
<td>arXiv</td>
<td>2024-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10447454">Towards Building The Federatedgpt: Federated Instruction Tuning</a></strong> </td>
<td>ICASSP</td>
<td>2024-03</td>
<td><img src="https://img.shields.io/github/stars/JayZhang42/FederatedGPT-Shepherd" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10447662">Communication-Efficient Personalized Federated Learning for Speech-to-Text Tasks</a></strong> </td>
<td>ICASSP</td>
<td>2024-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2403.06131">FedPIT: Towards Privacy-preserving and Few-shot Federated Instruction Tuning</a></strong> </td>
<td>arXiv</td>
<td>2024-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=06quMTmtRV">SLoRA: Federated Parameter Efficient Fine-Tuning of Language Models</a></strong> </td>
<td>FL@FM-NeurIPS</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2310.13283">pFedLoRA: Model-Heterogeneous Personalized Federated Learning with LoRA Tuning</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2307.13896">Low-Parameter Federated Learning with Large Language Models</a></strong> </td>
<td>arXiv</td>
<td>2023-07</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

#### Split Learning (9)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/11180881">Federated Fine-Tuning of LLMs: Framework Comparison and Research Directions</a></strong> </td>
<td>IEEE Commun. Mag.</td>
<td>2025-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/11045165">Split Fine-Tuning for Large Language Models in Wireless Networks</a></strong> </td>
<td>IEEE JSTSP</td>
<td>2025-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.emnlp-main.303/">Safely Learning with Private Data: A Federated Learning Framework for Large Language Model</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><img src="https://img.shields.io/github/stars/TAP-LLM/SplitFedLLM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10695888">FedsLLM: Federated Split Learning for Large Language Models Over Communication Networks</a></strong> </td>
<td>Ucom</td>
<td>2024-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2407.00952">SplitLoRA: A Split Parameter-Efficient Fine-Tuning Framework for Large Language Models</a></strong> </td>
<td>arXiv</td>
<td>2024-07</td>
<td><img src="https://img.shields.io/github/stars/FDU-INC/SplitFM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://icml.cc/virtual/2024/poster/34071">Enhancing Storage and Computational Efficiency in Federated Multimodal Learning for Large-Scale Models</a></strong> </td>
<td>ICML</td>
<td>2024-07</td>
<td><img src="https://img.shields.io/github/stars/M2FedSA/M-2FedSA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2403.16050">Heterogeneous Federated Learning with Splited Language Model</a></strong> </td>
<td>arXiv</td>
<td>2024-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10041745">Privacy-Preserving Split Learning for Large-Scaled Vision Pre-Training</a></strong> </td>
<td>TIFS</td>
<td>2023-02</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/9892845">Federated Split BERT for Heterogeneous Text Classification</a></strong> </td>
<td>IJCNN</td>
<td>2022</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Zeroth-Order Optimization (9)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=omrLHFzC37">Achieving Dimension-Free Communication in Federated Learning via Zeroth-Order Optimization</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2501.17610">FeedSign: Robust Full-parameter Federated Fine-tuning of Large Models with Extremely Low Communication Overhead of One Bit</a></strong> </td>
<td>arXiv</td>
<td>2025-01</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.1145/3637528.3671865">On the Convergence of Zeroth-Order Federated Tuning for Large Language Models</a></strong> </td>
<td>KDD</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/alibaba/FederatedScope" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2312.06353">Federated Full-Parameter Tuning of Billion-Sized Language Models with Communication Cost under 18 Kilobytes</a></strong> </td>
<td>ICML</td>
<td>2024-07</td>
<td><img src="https://img.shields.io/github/stars/alibaba/FederatedScope" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.01467">FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models</a></strong> </td>
<td>ICML</td>
<td>2024-07</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://www.usenix.org/conference/atc24/presentation/xu-mengwei">FwdLLM: Efficient Federated Finetuning of Large Language Models with Perturbed Inferences</a></strong> </td>
<td>ATC</td>
<td>2024-07</td>
<td><img src="https://img.shields.io/github/stars/UbiquitousLearning/FwdLLM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.findings-naacl.286.pdf">Personalized Federated Learning for Text Classification with Gradient-Free Prompt Tuning</a></strong> </td>
<td>NAACL</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.05143">ZooPFL: Exploring Black-box Foundation Models for Personalized Federated Learning</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.03123">Efficient Federated Prompt Tuning for Black-box Large Pre-trained Models</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

## Adaptability

### Domain-Centric Adaptation

#### Multi-Domain Adaptation (7)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=6SIVFmjIm4">Enhancing Foundation Models with Federated Domain Knowledge Infusion</a></strong> </td>
<td>ICML</td>
<td>2025-07</td>
<td><img src="https://img.shields.io/github/stars/JackqqWang/fedag" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=3wEGdrV5Cb">Enhancing Federated Domain Adaptation with Multi-Domain Prototype-Based Federated Fine-Tuning</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2025.coling-main.581/">FedCSR: A Federated Framework for Multi-Platform Cross-Domain Sequential Recommendation with Dual Contrastive Learning</a></strong> </td>
<td>COLING</td>
<td>2025-01</td>
<td><img src="https://img.shields.io/github/stars/zdy769243418/FedCSR-v1" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/9be9407431b7ff8cc04cae5460fcb7ab-Paper-Conference.pdf">DoFIT: Domain-aware Federated Instruction Tuning with Alleviated Catastrophic Forgetting</a></strong> </td>
<td>NeurIPS</td>
<td>2024-09</td>
<td><img src="https://img.shields.io/github/stars/1xbq1/DoFIT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10557150">Adapter-based Selective Knowledge Distillation for Federated Multi-domain Meeting Summarization</a></strong> </td>
<td>TASLP</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2403.08506">DiPrompT: Disentangled Prompt Tuning for Multiple Latent Domain Generalization in Federated Learning</a></strong> </td>
<td>CVPR</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29434">Federated Adaptive Prompt Tuning for Multi-Domain Collaborative Learning</a></strong> </td>
<td>AAAI</td>
<td>2024-03</td>
<td><img src="https://img.shields.io/github/stars/leondada/FedAPT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
</tbody>
</table>

### Client-Centric Adaptation

#### Preference-Aware Adaptation (3)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2412.15538">FedRLHF: A Convergence-Guaranteed Federated Framework for Privacy-Preserving and Personalized RLHF</a></strong> </td>
<td>AAMAS</td>
<td>2025-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=mqNKiEB6pd">Towards Federated RLHF with Aggregated Client Preference for LLMs</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/HarliWu/FedBiscuit" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2502.14187">Federated Fine-Tuning of Large Language Models: Kahneman-Tversky vs. Direct Preference Optimization</a></strong> </td>
<td>arXiv</td>
<td>2025-02</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

#### Personalization (9)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2412.15538">FedRLHF: A Convergence-Guaranteed Federated Framework for Privacy-Preserving and Personalized RLHF</a></strong> </td>
<td>AAMAS</td>
<td>2025-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=iX3uESGdsO">Selective Aggregation for Low-Rank Adaptation in Federated Learning</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/Pengxin-Guo/FedSA-LoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=nkwPiBSw1f">Dual-Personalizing Adapter for Federated Foundation Models</a></strong> </td>
<td>NeurIPS</td>
<td>2024-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=TXtRWPZIZ0">FedSelect: Customized Selection of Parameters for Fine-Tuning during Personalized Federated Learning</a></strong> </td>
<td>CVPR</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10447662">Communication-Efficient Personalized Federated Learning for Speech-to-Text Tasks</a></strong> </td>
<td>ICASSP</td>
<td>2024-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10389738">Joint Federated Learning and Personalization for on-Device ASR</a></strong> </td>
<td>ASRU</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10389620">Importance of Smoothness Induced by Optimizers in Fl4Asr: Towards Understanding Federated Learning for End-To-End ASR</a></strong> </td>
<td>ASRU</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2310.13283">pFedLoRA: Model-Heterogeneous Personalized Federated Learning with LoRA Tuning</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="http://sites.computer.org/debull/A23mar/p52.pdf">FedCLIP: Fast Generalization and Personalization for CLIP in Federated Learning</a></strong> </td>
<td>IEEE DEB</td>
<td>2023-03</td>
<td><img src="https://img.shields.io/github/stars/microsoft/PersonalizedFL" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
</tbody>
</table>

#### Clustering (4)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2508.19078">Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices</a></strong> </td>
<td>Eurosys</td>
<td>2026-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2024.findings-naacl.98">FedLFC: Towards Efficient Federated Multilingual Modeling with LoRA-based Language Family Clustering</a></strong> </td>
<td>NAACL</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=JDmAymuFFQ">FL-TAC: Enhanced Fine-Tuning in Federated Learning via Low-Rank, Task-Specific Adapter Clustering</a></strong> </td>
<td>LLMAgents@ICLR</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.1145/3485447.3511988">FedKC: Federated Knowledge Composition for Multilingual Natural Language Understanding</a></strong> </td>
<td>WWW</td>
<td>2022-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

## Trustworthiness

### IP Protection

#### Black-Box Tuning (4)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.01467">FedBPT: Efficient Federated Black-box Prompt Tuning for Large Language Models</a></strong> </td>
<td>ICML</td>
<td>2024-07</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2024.findings-naacl.286.pdf">Personalized Federated Learning for Text Classification with Gradient-Free Prompt Tuning</a></strong> </td>
<td>NAACL</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.05143">ZooPFL: Exploring Black-box Foundation Models for Personalized Federated Learning</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2310.03123">Efficient Federated Prompt Tuning for Black-box Large Pre-trained Models</a></strong> </td>
<td>arXiv</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Privacy Preservation

#### Privacy Attack (6)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10818586">Data Reconstruction and Protection in Federated Learning for Fine-Tuning Large Language Models</a></strong> </td>
<td>IEEE TBD</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/97d008f7873b8dd55cb6dd343fc4386f-Paper-Conference.pdf">Privacy Backdoors: Enhancing Membership Inference through Poisoning Pre-trained Models</a></strong> </td>
<td>NeurIPS</td>
<td>2024-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.lrec-main.1227">Revisiting Data Reconstruction Attacks on Real-world Dataset for Federated Natural Language Understanding</a></strong> </td>
<td>LREC-COLING</td>
<td>2024-05</td>
<td><img src="https://img.shields.io/github/stars/SMILELab-FL/FedAttack" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://proceedings.mlr.press/v238/vu24a.html"> Analysis of Privacy Leakage in Federated Large Language Models </a></strong> </td>
<td>AISTATS</td>
<td>2024-05</td>
<td><img src="https://img.shields.io/github/stars/vunhatminh/FL_Attacks" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=A9WQaxYsfx">Panning for Gold in Federated Learning: Targeted Text Extraction under Arbitrarily Large-Scale Aggregation</a></strong> </td>
<td>ICLR</td>
<td>2023-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/35b5c175e139bff5f22a5361270fce87-Paper-Conference.pdf">Recovering Private Text in Federated Learning of Language Models</a></strong> </td>
<td>NeurIPS</td>
<td>2022-11</td>
<td><img src="https://img.shields.io/github/stars/Princeton-SysML/FILM" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
</tbody>
</table>

#### Privacy-Preserving Techniques (8)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://proceedings.mlr.press/v267/li25n.html">Clients Collaborate: Flexible Differentially Private Federated Learning with Guaranteed Improvement of Utility-Privacy Trade-off</a></strong> </td>
<td>ICML</td>
<td>2025-13--19 Jul</td>
<td><img src="https://img.shields.io/github/stars/6lyc/FedCEO_Collaborate-with-Each-Other" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=Equ277PBN0">Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models</a></strong> </td>
<td>ICLR</td>
<td>2025-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10818586">Data Reconstruction and Protection in Federated Learning for Fine-Tuning Large Language Models</a></strong> </td>
<td>IEEE TBD</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2024.findings-emnlp.615/">Promoting Data and Model Privacy in Federated Learning through Quantized LoRA</a></strong> </td>
<td>EMNLP</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://dl.acm.org/doi/abs/10.1145/3682068">Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning</a></strong> </td>
<td>ACM TMIS</td>
<td>2024-08</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://icml.cc/virtual/2024/poster/35060">PrE-Text: training language models on private federated data in the age of LLMs</a></strong> </td>
<td>ICML</td>
<td>2024-07</td>
<td><img src="https://img.shields.io/github/stars/houcharlie/PrE-Text" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=NLPzL6HWNl">Improving LoRA in Privacy-preserving Federated Learning</a></strong> </td>
<td>ICLR</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2023.acl-industry.60">Federated Learning of Gboard Language Models with Differential Privacy</a></strong> </td>
<td>ACL</td>
<td>2023-07</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Attack Robustness

#### Poisoning Attack (8)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=sYNWqQYJhz">Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models</a></strong> </td>
<td>ICLR</td>
<td>2025-01</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2501.18416">Exploring Potential Prompt Injection Attacks in Federated Military LLMs and Their Mitigation</a></strong> </td>
<td>arXiv</td>
<td>2025-01</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10776777">SecFFT: Safeguarding Federated Fine-Tuning for Large Vision Language Models against Covert Backdoor Attacks in IoRT Networks</a></strong> </td>
<td>IEEE IoTJ</td>
<td>2024-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2411.19335">PEFT-as-an-Attack! Jailbreaking Language Models during Federated Parameter-Efficient Fine-Tuning</a></strong> </td>
<td>arXiv</td>
<td>2024-11</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2410.17573">Securing Federated Learning Against Novel and Classic Backdoor Threats During Foundation Model Integration</a></strong> </td>
<td>arXiv</td>
<td>2024-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2409.14805">SDBA: A Stealthy and Long-Lasting Durable Backdoor Attack in Federated Learning</a></strong> </td>
<td>arXiv</td>
<td>2024-09</td>
<td><img src="https://img.shields.io/github/stars/ict-convergence-security-lab-chosun/sdba" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://link.springer.com/chapter/10.1007/978-981-97-2259-4_13">Unveiling Backdoor Risks Brought by Foundation Models in Heterogeneous Federated Learning</a></strong> </td>
<td>PAKDD</td>
<td>2024-04</td>
<td><img src="https://img.shields.io/github/stars/lixi1994/backdoor_FM_hete_FL" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=BrcHuO2BVc">Backdoor Threats from Compromised Foundation Models to Federated Learning</a></strong> </td>
<td>FL@FM-NeurIPS</td>
<td>2023-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

## Application

### Multilingualism (9)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://www.nature.com/articles/s41746-025-01434-3">Real world federated learning with a knowledge distilled transformer for cardiac CT imaging</a></strong> </td>
<td>NPJ Digital Medicine</td>
<td>2025-02</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://2024.naacl.org/program/accepted_papers/">Generalizable Multilingual Hate Speech Detection on Low Resource Indian Languages using Fair Selection in Federated Learning</a></strong> </td>
<td>NAACL</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://openreview.net/forum?id=zzqn5G9fjn">Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages</a></strong> </td>
<td>ICLR</td>
<td>2024-05</td>
<td><img src="https://img.shields.io/github/stars/Ryan0v0/multilingual_borders" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.1145/3589335.3651931">Only Send What You Need: Learning to Communicate Efficiently in Federated Multilingual Machine Translation</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.1145/3589335.3651933">FedHLT: Efficient Federated Low-Rank Adaption with Hierarchical Language Tree for Multilingual Modeling</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2023.findings-acl.327">Communication Efficient Federated Learning for Multilingual Neural Machine Translation with Adapter</a></strong> </td>
<td>ACL</td>
<td>2023-07</td>
<td><img src="https://img.shields.io/github/stars/lancopku/FedMNMT" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://proceedings.mlr.press/v209/manoel23a.html">Federated Multilingual Models for Medical Transcript Analysis</a></strong> </td>
<td>CHIL</td>
<td>2023-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2022.naacl-main.101">Pretrained Models for Multilingual Federated Learning</a></strong> </td>
<td>NAACL</td>
<td>2022-07</td>
<td><img src="https://img.shields.io/github/stars/orionw/Multilingual-Federated-Learning" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.1145/3485447.3511988">FedKC: Federated Knowledge Composition for Multilingual Natural Language Understanding</a></strong> </td>
<td>WWW</td>
<td>2022-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Speech (4)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10447662">Communication-Efficient Personalized Federated Learning for Speech-to-Text Tasks</a></strong> </td>
<td>ICASSP</td>
<td>2024-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10389738">Joint Federated Learning and Personalization for on-Device ASR</a></strong> </td>
<td>ASRU</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10389620">Importance of Smoothness Induced by Optimizers in Fl4Asr: Towards Understanding Federated Learning for End-To-End ASR</a></strong> </td>
<td>ASRU</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=ozN92d7CHX">Federated Learning for Speech Recognition: Revisiting Current Trends Towards Large-Scale ASR</a></strong> </td>
<td>FL@FM-NeurIPS</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Recommendation Systems (7)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2025.findings-naacl.155/">A Federated Framework for LLM-based Recommendation</a></strong> </td>
<td>NAACL</td>
<td>2025-04</td>
<td><img src="https://img.shields.io/github/stars/Polaris-JZ/FELLRec" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://aclanthology.org/2025.coling-main.581/">FedCSR: A Federated Framework for Multi-Platform Cross-Domain Sequential Recommendation with Dual Contrastive Learning</a></strong> </td>
<td>COLING</td>
<td>2025-01</td>
<td><img src="https://img.shields.io/github/stars/zdy769243418/FedCSR-v1" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/document/10825302">Federated Recommendation via Hybrid Retrieval Augmented Generation</a></strong> </td>
<td>IEEE BigData</td>
<td>2024-12</td>
<td><img src="https://img.shields.io/github/stars/huiminzeng/GPT-FedRec" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2404.11536">Federated Adaptation for Foundation Model-based Recommendations</a></strong> </td>
<td>IJCAI</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/Zhangcx19/IJCAI-24-FedPA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2406.00004">Navigating the Future of Federated Recommendation Systems with Foundation Models</a></strong> </td>
<td>arXiv</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.1145/3589334.3645337">Prompt-enhanced Federated Content Representation Learning for Cross-domain Recommendation</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><img src="https://img.shields.io/github/stars/Ckano/PFCR" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2402.01124">TransFR: Transferable Federated Recommendation with Pre-trained Language Models</a></strong> </td>
<td>arXiv</td>
<td>2024-02</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Domain Specific (11)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://www.nature.com/articles/s41746-025-01434-3">Real world federated learning with a knowledge distilled transformer for cardiac CT imaging</a></strong> </td>
<td>NPJ Digital Medicine</td>
<td>2025-02</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2404.11536">Federated Prompt Learning for Weather Foundation Models on Devices</a></strong> </td>
<td>IJCAI</td>
<td>2024-08</td>
<td><img src="https://img.shields.io/github/stars/shengchaochen82/FedPoD" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://link.springer.com/article/10.1007/s11280-024-01266-3">Foundation models matter: federated learning for multi-center tuberculosis diagnosis via adaptive regularization and model-contrastive learning</a></strong> </td>
<td>WWW</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10445933">Prompt-Based Personalized Federated Learning for Medical Visual Question Answering</a></strong> </td>
<td>ICASSP</td>
<td>2024-04</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2403.05408">FedFMS: Exploring Federated Foundation Models for Medical Image Segmentation</a></strong> </td>
<td>MICCAI</td>
<td>2024</td>
<td><img src="https://img.shields.io/github/stars/LIU-YUXI/FedFMS" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.24963/ijcai.2023/393">Prompt Federated Learning for Weather Forecasting: Toward Foundation Models on Meteorological Data</a></strong> </td>
<td>IJCAI</td>
<td>2023-8</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2023.emnlp-main.734">FedTherapist: Mental Health Monitoring with User-Generated Linguistic Expressions on Smartphones via Federated Learning</a></strong> </td>
<td>EMNLP</td>
<td>2023-12</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://doi.org/10.48550/arXiv.2309.08173">FedJudge: Federated Legal Large Language Model</a></strong> </td>
<td>arXiv</td>
<td>2023-09</td>
<td><img src="https://img.shields.io/github/stars/yuelinan/FedJudge" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2023.acl-long.193">FEDLEGAL: The First Real-World Federated Learning Benchmark for Legal NLP</a></strong> </td>
<td>ACL</td>
<td>2023-07</td>
<td><img src="https://img.shields.io/github/stars/SMILELab-FL/FedLegal" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/document/10205077">Learning Federated Visual Prompt in Null Space for MRI Reconstruction</a></strong> </td>
<td>CVPR</td>
<td>2023-06</td>
<td><img src="https://img.shields.io/github/stars/chunmeifeng/FedPR" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://proceedings.mlr.press/v209/manoel23a.html">Federated Multilingual Models for Medical Transcript Analysis</a></strong> </td>
<td>CHIL</td>
<td>2023-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

## Resources

### Surveys (11)

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://www.ijcai.org/proceedings/2025/1196">Federated Low-Rank Adaptation for Foundation Models: A Survey</a></strong> </td>
<td>IJCAI</td>
<td>2025-08</td>
<td><img src="https://img.shields.io/github/stars/Lydia-yang/Awesome-Federated-LoRA" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2503.12016">A Survey on Federated Fine-tuning of Large Language Models</a></strong> </td>
<td>arXiv</td>
<td>2025-03</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2404.15381">Advances and Open Challenges in Federated Learning with Foundation Models</a></strong> </td>
<td>IEEE COMST</td>
<td>2025-01</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10759678">Towards Federated Large Language Models: Motivations, Methods, and Future Directions</a></strong> </td>
<td>IEEE COMST</td>
<td>2024-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10733964">Federated Large Language Model: Solutions, Challenges and Future Directions</a></strong> </td>
<td>IEEE WC</td>
<td>2024-10</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2409.15723">Federated Large Language Models: Current Progress and Future Directions</a></strong> </td>
<td>arXiv</td>
<td>2024-09</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://www.ijcai.org/proceedings/2024/0919.pdf">A Survey on Efficient Federated Learning Methods for Foundation Model Training</a></strong> </td>
<td>IJCAI</td>
<td>2024-08</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://arxiv.org/abs/2406.12844">Synergizing Foundation Models and Federated Learning: A Survey</a></strong> </td>
<td>arXiv</td>
<td>2024-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://aclanthology.org/2024.lrec-main.630">Federated Foundation Models: Privacy-Preserving and Collaborative Learning for Large Models</a></strong> </td>
<td>LREC-COLING</td>
<td>2024-05</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/10558823">The Role of Federated Learning in a Wireless World with Foundation Models</a></strong> </td>
<td>IEEE WC</td>
<td>2024</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><a href="https://doi.org/10.48550/arXiv.2306.15546">When foundation model meets federated learning: Motivations, challenges, and future directions</a></strong> </td>
<td>arXiv</td>
<td>2023-06</td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

### Frameworks (11)

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Venue</th>
<th>Year</th>
<th>GitHub</th>
<th>Developed by</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><a href="https://www.vldb.org/pvldb/vol16/p1059-li.pdf">FederatedScope: A Flexible Federated Learning Platform for Heterogeneity</a></strong> </td>
<td>VLDB</td>
<td>2023-09</td>
<td><img src="https://img.shields.io/github/stars/alibaba/FederatedScope" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/Alibaba-white?logo=alibabadotcom" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="http://jmlr.org/papers/v24/22-0440.html">FedLab: A Flexible Federated Learning Framework</a></strong> </td>
<td>JMLR</td>
<td>2023-01</td>
<td><img src="https://img.shields.io/github/stars/SMILELab-FL/FedLab" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/SMILELab-white?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MTAgNDEwIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA0MTAgNDEwIiB4bWw6c3BhY2U9InByZXNlcnZlIj48c3R5bGU+LnN0MHtmaWxsOiNmZjUyMDd9LnN0MSwuc3Qye2ZpbGw6I2UwMTkxNDtmaWxsLXJ1bGU6ZXZlbm9kZDtjbGlwLXJ1bGU6ZXZlbm9kZH0uc3Qye2ZpbGw6IzEzODljNH08L3N0eWxlPjxyZWN0IHg9IjE2OSIgeT0iMTYxIiBjbGFzcz0ic3QwIiB3aWR0aD0iNTMiIGhlaWdodD0iNTEiLz48cGF0aCBjbGFzcz0ic3QxIiBkPSJNMzkxIDkwYy01IDIwLTQxIDE1My0xNTggMTk3LTE5IDctNzkgMzAtMTI5IDMtNzMtNDAtNzItMTU0LTgwLTE1M3MtOCAxMDcgNTggMTcyYzM1IDM0IDk2IDYxIDE0OCA0MyA4MS0yNyAxMTEtMTQ4IDE1My0xMzggMTIgMyAxNyAxNCAyMyAxMi01LTQ1LTEwLTkxLTE1LTEzNiIvPjxyZWN0IHg9IjgxIiB5PSI5NiIgY2xhc3M9InN0MiIgd2lkdGg9IjU0IiBoZWlnaHQ9IjU0Ii8+PHJlY3QgeD0iMjIyIiB5PSI4NyIgY2xhc3M9InN0MiIgd2lkdGg9Ijc0IiBoZWlnaHQ9Ijc0Ii8+PC9zdmc+" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="http://iopscience.iop.org/article/10.1088/1361-6560/ac97d9">OpenFL: the open federated learning library</a></strong> </td>
<td>PMB</td>
<td>2022-10</td>
<td><img src="https://img.shields.io/github/stars/securefederatedai/openfl" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/Intel-white?logo=Intel" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://openreview.net/forum?id=hD9QaIQTL_f">NVIDIA FLARE: Federated Learning from Simulation to Real-World</a></strong> </td>
<td>FL@NeurIPS</td>
<td>2022-07</td>
<td><img src="https://img.shields.io/github/stars/NVIDIA/NVFlare" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/Nvidia-white?logo=nvidia" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://proceedings.mlr.press/v162/lai22a.html">FedScale: Benchmarking Model and System Performance of Federated Learning at Scale</a></strong> </td>
<td>ICML</td>
<td>2022-07</td>
<td><img src="https://img.shields.io/github/stars/SymbioticLab/FedScale" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/SymbioticLab-white?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgNDAwIj48c3R5bGU+LmF7ZmlsbDojMjMxZjIwfS5ie2ZpbGw6I2YzNmMyMX0uYSwuYntmaWxsLXJ1bGU6ZXZlbm9kZH08L3N0eWxlPjxwYXRoIGNsYXNzPSJhIiBkPSJtMjIzIDE0NiA4NC0xMzUgMy00LTQ1IDEtNjAgMTA3TTIyOCAxNTZsMTggMzEgODUtMTQ3LTIyLTMwTTE1MiAyMDkgNjYgMzU2bDIyIDMyIDgzLTE0OE0xNzQgMjUyIDkyIDM4OWgyMTVsMjMtMzItMTgzIDYgNDUtODEiLz48cGF0aCBjbGFzcz0iYiIgZD0iTTI1NCA2IDg5IDcgNjYgNDBsMTczLTRNMjM0IDQ0IDY2IDQwbDE1NiAyNzRoMzhMMTI4IDc1bDg5LTIiLz48cGF0aCBjbGFzcz0iYiIgZD0ibTEzOCA4MyAxMzYgMjM3LTkxIDEtMTggMzAgMTY4IDNMMTc3IDg0Ii8+PC9zdmc+" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://ieeexplore.ieee.org/abstract/document/9826069">Scalable federated machine learning with FEDn</a></strong> </td>
<td>CCGrid</td>
<td>2022-05</td>
<td><img src="https://img.shields.io/github/stars/scaleoutsystems/fedn" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/Scaleout-white?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMjM2Ij48c3R5bGU+LmF7ZmlsbDojMWIxYjFiO2ZpbGwtcnVsZTpldmVub2RkfTwvc3R5bGU+PHBhdGggY2xhc3M9ImEiIGQ9Ik0xMDMgODRjLTE0IDUtMjMgMTctMjUgMjktMyAyMiAxNiA0MiAzNCA0NSAxNiAyIDI4LTEwIDUyLTMzIDgxLTc3IDkxLTgzIDEwNC04NiAyOS02IDY5IDQgOTAgMzQgMjYgMzggNiA4MyA1IDg2LTIwIDMxLTUyIDQ4LTg0IDQ0LTI1LTMtNDEtMTctNDgtMjMtMyAzLTUgNi04IDEwIDMgMyA0MSAzNiA5MCAyNCA0Mi0xMSA2OC01MCA3MS04NiAxLTcgMy0zMS0xMi01Ni0yMS0zNS02NC01Mi05OS00Ni0yNiA0LTQ5IDI2LTk2IDcxLTM4IDM2LTUxIDUzLTY2IDQ5LTE0LTQtMjUtMjUtMTgtMzggNi0xMCAyNC0xNSA0Mi03IDItMiA0LTUgNi03LTEwLTEwLTI1LTE0LTM4LTEwbTMyIDgzYzQ2LTE3IDY0LTc4IDEzNC0xMTIgMjEtMTAgNTIgMSA3MCAyMCAxNSAxNiAxNyAzNiAxNyA0NCAxIDI1LTE1IDUyLTQyIDYzLTI0IDEwLTUyIDQtNzEtMTQgMy0zIDUtNiA3LTkgNSAzIDIyIDE2IDQ0IDEyIDMxLTUgNTUtNDAgNDgtNjctNi0yNC0zNy00NS02Mi0zOC00NiAxMy01NyA1OC0xMjYgMTA5LTE2IDEyLTI5IDE1LTQzIDE0LTMxLTMtNjQtMzktNjEtNzcgMC00IDMtMzAgMjYtNDYgMjQtMTcgNTktMTYgODcgNGwtMTAgMTFjLTI3LTIyLTY0LTE3LTgwIDQtMjEgMjctNCA3MSAyNCA4MyAxNSA3IDMxIDIgMzgtMW0xMzEtNzljNS0zIDE3LTkgMjktNiAxNiA0IDMzIDIwIDMxIDQxLTEgMTMtOSAyNS0yMiAzMS0xNCA2LTMxIDMtNDItOCAyLTIgNS01IDctOCAxIDEgMTMgMTEgMjcgNiAxMy01IDIxLTIwIDE2LTM3LTItNC02LTEwLTEzLTEyLTExLTQtMjMgMS0zMiA4LTQ1IDM0LTczIDkzLTEyOSAxMTAtNDEgMTMtMTAyLTIwLTExNi03M0M5IDk0IDQxIDM3IDkwIDI5YzUwLTkgODkgMTkgOTMgMjItMyA0LTcgNy0xMCAxMS0zOS0zMC05MC0yNy0xMTkgMi0yMCAyMC0yNyA1Mi0xOSA3OSAxMSAzNyA0OCA2MyA5MSA2MSA1NS04IDk1LTg3IDE0MC0xMTYiLz48L3N2Zz4=" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2203.13789">FLUTE: A Scalable Extensible Framework for High-Performance Federated Learning Simulations</a></strong> </td>
<td>FL@NeurIPS</td>
<td>2022-03</td>
<td><img src="https://img.shields.io/github/stars/microsoft/msrflute" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/Microsoft-white?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMyAyMyI+PHBhdGggZmlsbD0iI2YzZjNmMyIgZD0iTTAgMGgyM3YyM0gweiIvPjxwYXRoIGZpbGw9IiNmMzUzMjUiIGQ9Ik0xIDFoMTB2MTBIMXoiLz48cGF0aCBmaWxsPSIjODFiYzA2IiBkPSJNMTIgMWgxMHYxMEgxMnoiLz48cGF0aCBmaWxsPSIjMDVhNmYwIiBkPSJNMSAxMmgxMHYxMEgxeiIvPjxwYXRoIGZpbGw9IiNmZmJhMDgiIGQ9Ik0xMiAxMmgxMHYxMEgxMnoiLz48L3N2Zz4=" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="http://jmlr.org/papers/v22/20-815.html">FATE: An Industrial Grade Platform for Collaborative Learning With Data Protection</a></strong> </td>
<td>JMLR</td>
<td>2021-08</td>
<td><img src="https://img.shields.io/github/stars/FederatedAI/FATE" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/Webank-white?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgNDgyIj48c3R5bGU+LmEsLmJ7ZmlsbC1ydWxlOmV2ZW5vZGR9LmF7ZmlsbDojMzYzNTM1fS5ie2ZpbGw6I2QwMzExZX08L3N0eWxlPjxwYXRoIGNsYXNzPSJhIiBkPSJNMjIzIDdjLTg3IDMtMTM2IDk0LTEzOSA5OS0yMyAwLTQxIDYtNDMgMTUtMyAxMCAxNiAyNyA0OCAzNy0yNSA0MC00OSA1Ny02MCA4M0M2IDI5MyAwIDMzNyA4IDM2M2M5IDMyIDM5IDQ2IDMyIDY1LTYgMTctMzIgMTYtMzMgMjMgMCAxNyAxNjQgMjEgMjYwIDIzIDM0IDEgNzkgMSA5MC0yMSAxMS0yMyAzLTQ4LTMtODEtMTktMTA3IDUxLTE0MyAzNS0yMjRDMzc1IDgxIDMwNiA0IDIyMyA3bS01NyAyNTZjLTMyIDg1IDE5IDE2NC01IDE3OC0yMCAxMi04Mi0zMy0xMDMtOTUtMzEtOTQgNTMtMTgxIDU2LTE4NSAyMi03MiA3Ny0xMDQgMTA2LTkzIDI0IDkgMzkgNTIgMzMgMTAwLTI4IDE2LTY5IDQ2LTg3IDk1Ii8+PHBhdGggY2xhc3M9ImEiIGQ9Ik0xODYgMTA2Yy04LTUtMTgtNC0yNSAxLTkgOC05IDIzLTEgMzEgOSA5IDI2IDYgMzItNSA1LTkgMi0yMS03LTI3Ii8+PHBhdGggY2xhc3M9ImIiIGQ9Ik0zOTAgMTQ4Yy0yNCA2LTQ5IDExLTc3IDE1LTkxIDEyLTE3MSA0LTIzMS05LTExIDIyLTI5IDQxLTQwIDYzIDY2IDE4IDEyOSAyOSAxNjkgMzMgODggOCAxNTAgMTMgMTc1LTIzIDE3LTIzIDExLTU2IDQtNzkiLz48L3N2Zz4=" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://link.springer.com/chapter/10.1007/978-3-030-70604-3_5">Pysyft: A library for easy federated learning</a></strong> </td>
<td>FLS</td>
<td>2021-06</td>
<td><img src="https://img.shields.io/github/stars/OpenMined/PySyft" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/OpenMined-white?logo=OpenMined" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="even">
<td><strong><a href="https://flower.ai/">Flower: A friendly federated learning research framework</a></strong> </td>
<td>Arxiv</td>
<td>2020-07</td>
<td><img src="https://img.shields.io/github/stars/adap/flower" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/Flower-white?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgNDAxIj48c3R5bGU+LmEsLmJ7ZmlsbC1ydWxlOmV2ZW5vZGQ7Y2xpcC1ydWxlOmV2ZW5vZGR9LmF7ZmlsbDojMmMyZDM0fS5ie2ZpbGw6I2ZmZn0uY3tmaWxsOiMyMzFmMjB9PC9zdHlsZT48cGF0aCBjbGFzcz0iYSIgZD0ibTI5IDE5Mi0xNy0zMiAyOC02MiAzNi0zIDEzLTMwIDQ1LTIwIDMyIDEwIDE2LTIxaDYwbDE5IDIxIDI4LTcgNTEgMzIgMiAyOSAzMCA5IDE4IDYxLTE5IDI5IDEzIDMyLTIzIDU3LTM0IDQtNiAzMi01OCAyMi0yMi04LTIyIDIwaC02N2wtMTktMjItMjMgNy01NC0yOS0xLTM2LTM1LTE0LTktNTV6Ii8+PHBhdGggY2xhc3M9ImIiIGQ9Im02OSAxOTItMjEtMzQgMTUtMjkgMzctMyAxNC0zNiAyMi0xMCAzOSAxNCAyNC0yOGgyNmwyNCAyNSAzNC04IDI0IDE0IDQgMzggMzMgOSAxMCAzMC0yMSAzMSAxNSAzNy05IDI0LTQwIDctNiAzNS0zNCAxNC0zMC05LTIzIDIxaC0zOGwtMjQtMjctMzEgOS0yNS0xNnYtMzZsLTM3LTE1LTQtMjR6Ii8+PHBhdGggY2xhc3M9ImMiIGQ9Im0yNTIgMTM4IDI5IDI5LTEgNTEtMjkgMjgtODIgMS0yOS0yOC0xLTUyIDI5LTI5eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Im0xODMgMjE0LTEwLTEwdi0yNGwxMC0xMGg1NWwxMCAxMHYyNGwtMTAgOXoiLz48L3N2Zz4=" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
<tr class="odd">
<td><strong><a href="https://arxiv.org/abs/2007.13518">FedML: A Research Library and Benchmark for Federated Machine Learning</a></strong> </td>
<td>SpicyFL</td>
<td>2020-07</td>
<td><img src="https://img.shields.io/github/stars/FedML-AI/FedML" alt="GitHub Repo stars" style="vertical-align: middle; width: auto; height: auto;"/></td>
<td><img src="https://img.shields.io/badge/FedML-white?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NTAgNTQ2Ij48c3R5bGU+LnMwe2ZpbGw6IzZlNjNhNH0uczF7ZmlsbDojZTA2NzVjfS5zMntmaWxsOiNlZGI5NTB9LnMze2ZpbGw6IzYxYjg1Mn08L3N0eWxlPjxwYXRoIGNsYXNzPSJzMCIgZD0iTTI3NiAyMTJzODYtODUgODYtMTI0YzAtMzQtMzktNjEtODYtNjFzLTg2IDI3LTg2IDYxYzAgMzkgODYgMTI0IDg2IDEyNCIvPjxwYXRoIGNsYXNzPSJzMSIgZD0iTTIxMiAyODZzLTg2LTg2LTEyNC04NmMtMzQgMC02MSAzOS02MSA4NnMyNyA4NiA2MSA4NmMzOSAwIDEyNC04NiAxMjQtODYiLz48cGF0aCBjbGFzcz0iczIiIGQ9Ik0yNzYgMzM0cy04NiA4Ni04NiAxMjRjMCAzNCAzOSA2MSA4NiA2MXM4Ni0yNyA4Ni02MWMwLTM5LTg2LTEyNC04Ni0xMjQiLz48cGF0aCBjbGFzcz0iczMiIGQ9Ik0zNDAgMjg2czg2IDg2IDEyNCA4NmMzNCAwIDYxLTM5IDYxLTg2cy0yNy04Ni02MS04NmMtMzkgMC0xMjQgODYtMTI0IDg2Ii8+PC9zdmc+" alt="GitHub Repo stars" style="vertical-align: middle; width: 150px; height: auto;"/></td>
</tr>
</tbody>
</table>
