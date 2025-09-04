# Proceedings - Medical Video Question Answering 2024

#### Overview of TREC 2024 Medical video Question Answering (MedVidQA) Track

_Deepak Gupta,  Dina Demner-Fushman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_medvidqa.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_medvidqa.pdf)
??? abstract "Abstract"
	
	One of the key goals of artificial intelligence (AI) is the development of a multimodal system that facilitates communication with the visual world (image and video) using a natural language query. Earlier works on medical question answering primarily focused on textual and visual (image) modalities, which may be inefficient in answering questions requiring demonstration. In recent years, significant progress has been achieved due to the introduction of large-scale language-vision datasets and the development of efficient deep neural techniques that bridge the gap between language and visual understanding. Improvements have been made in numerous vision-and-language tasks, such as visual captioning visual question answering, and natural language video localization. Most of the existing work on language vision focused on creating datasets and developing solutions for open-domain applications. We believe medical videos may provide the best possible answers to many first aid, medical emergency, and medical education questions. With increasing interest in AI to support clinical decision-making and improve patient engagement, there is a need to explore such challenges and develop efficient algorithms for medical language-video understanding and generation. Toward this, we introduced new tasks to foster research toward designing systems that can understand medical videos to provide visual answers to natural language questions, and are equipped with multimodal capability to generate instruction steps from the medical video. These tasks have the potential to support the development of sophisticated downstream applications that can benefit the public and medical professionals.
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-2,
		author = {Deepak Gupta and Dina Demner-Fushman},
		title = {Overview of TREC 2024 Medical video Question Answering (MedVidQA) Track},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {coordinators},
		trec_runs = {},
		trec_tracks = {medvidqa},
		url = {https://trec.nist.gov/pubs/trec33/papers/Overview_medvidqa.pdf}
	}
	```

#### Doshisha University, Universität zu Lübeck and German Research Center for Artificial Intelligence at TRECVID 2024: QFISC Task

_Zihao Chen (Doshisha University), Falco Lentzsch (German Research Center for Artificial Intelligence), Nele S. Brügge (German Research Center for Artificial Intelligence), Frédéric Li (German Research Center for Artificial Intelligence), Miho Ohsaki (Doshisha University), Heinz Handels (German Research Center for Artificial Intelligence, University of Luebeck), Marcin Grzegorzek (German Research Center for Artificial Intelligence, University of Luebeck), Kimiaki Shirahama (Doshisha University)_

- :fontawesome-solid-user-group: **Participant:** [DoshishaUzlDfki](./participants.md#doshishauzldfki)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/DoshishaUzlDfki.medvidqa.pdf](https://trec.nist.gov/pubs/trec33/papers/DoshishaUzlDfki.medvidqa.pdf)
- :material-file-search: **Runs:** [chatGPT_zeroshot_prompt](./runs.md#chatgpt_zeroshot_prompt) | [mistral_meta_prompt](./runs.md#mistral_meta_prompt) | [mistral_fewshot_prompt](./runs.md#mistral_fewshot_prompt) | [GPT_meta_prompt](./runs.md#gpt_meta_prompt) | [CoSeg_meta_prompt](./runs.md#coseg_meta_prompt)

??? abstract "Abstract"
	
	This paper presents the approaches proposed by the DoshishaUzlDfki team to address the Query-Focused Instructional Step Captioning (QFISC) task of TRECVID 2024. Given some RGB videos containing stepwise instructions, we explored several techniques to automatically identify the boundaries of each step, and provide a caption to it. More specifically, two different types of methods were investigated for temporal video segmentation. The first uses the CoSeg approach proposed by Wang et al. [9] based on Event Segmentation Theory, which hypothesises that video frames at the boundaries of steps are harder to predict since they tend to contain more significant visual changes. In detail, CoSeg detects event boundaries in the RGB video stream by finding the local maxima in the reconstruction error of a model trained to reconstruct the temporal contrastive embeddings of video snippets. The second type of approaches we tested exclusively relies on the audio modality, and is based on the hypothesis that information about step transitions is often semantically contained in the verbal transcripts of the videos. In detail, we used the WhisperX model [3] that isolates speech parts in the audio tracks of the videos, and converts them into timestamped text transcripts. The latter were then sent as input of a Large Language Model (LLM) with a carefully designed prompt requesting the LLM to identify step boundaries. Once the temporal video segmentation performed, we
sent the WhisperX transcripts corresponding to the video segments determined by both methods to a LLM instructed to caption them. The GPT4o and Mistral Large 2 LLMs were employed in our experiments for both segmentation and captioning. Our results show that the temporal segmentation methods based on audioprocessing significantly outperform the video-based one. More specifically, the best performances we obtained are yielded by our approach using GPT4o with zero-shot prompting for temporal segmentation. It achieves the top global performances of all runs submitted to the QFISC task in all evaluation metrics, except for precision whose best performance is obtained by our run using Mistral Large 2 with chain-of-thoughts prompting.
	

??? quote "Bibtex"
	```
	@inproceedings{DoshishaUzlDfki-trec2024-papers-proc-1,
		author = {Zihao Chen (Doshisha University), Falco Lentzsch (German Research Center for Artificial Intelligence), Nele S. Brügge (German Research Center for Artificial Intelligence), Frédéric Li (German Research Center for Artificial Intelligence), Miho Ohsaki (Doshisha University), Heinz Handels (German Research Center for Artificial Intelligence, University of Luebeck), Marcin Grzegorzek (German Research Center for Artificial Intelligence, University of Luebeck), Kimiaki Shirahama (Doshisha University)},
		title = {Doshisha University, Universität zu Lübeck and German Research Center for Artificial Intelligence at TRECVID 2024: QFISC Task},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {DoshishaUzlDfki},
		trec_runs = {chatGPT_zeroshot_prompt, mistral_meta_prompt, mistral_fewshot_prompt, GPT_meta_prompt, CoSeg_meta_prompt},
		trec_tracks = {medvidqa},
		url = {https://trec.nist.gov/pubs/trec33/papers/DoshishaUzlDfki.medvidqa.pdf}
	}
	```

