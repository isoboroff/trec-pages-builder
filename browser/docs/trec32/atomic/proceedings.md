# Proceedings - AToMiC 2023

#### TREC2023 AToMiC Overview

_Jheng-Hong Yang,  Carlos Lassance,  Rafael Sampaio de Rezende,  Krishna Srinivasan,  Miriam Redi,  Stéphane Clinchant,  Jimmy Lin_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_atomic.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_atomic.pdf)
??? abstract "Abstract"
	
	This paper presents an exploration of evaluating image–text re-trieval tasks designed for multimedia content creation, with a par-ticular focus on the dynamic interplay among various modalities,including text and images. The study highlights the pivotal roleof visual-textual multimodality, where elements such as photos,graphics, and diagrams are not merely ornamental but significantlyaugment, complement, or even reshape the meaning conveyed bytextual content. This integration of multiple modalities is central tocrafting immersive and captivating multimedia experiences. In thecontext of detailing the TREC initiative’s evaluation process for theyear, the paper introduces the AToMiC test collection, which servesas the foundational framework for evaluation. The authors delveinto the distinctive task design, elucidating the specific challengesand objectives that characterize this year’s evaluation. The paperfurther outlines the evaluation protocols, encompassing method-ologies such as pooling dependencies and the criteria employed forrelevance judgments. This overview offers valuable insights intothe intricate process of evaluating multimedia retrieval systems,underscoring the evolving complexity and interdisciplinary natureof this field.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLRSRCL23.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLRSRCL23,
		author = {Jheng{-}Hong Yang and Carlos Lassance and Rafael Sampaio de Rezende and Krishna Srinivasan and Miriam Redi and St{\'{e}}phane Clinchant and Jimmy Lin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC2023} AToMiC Overview},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Overview\_atomic.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLRSRCL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multimodal Learned Sparse Retrieval for Image Suggestion Task

_Thong Nguyen,  Mariya Hendriksen,  Andrew Yates_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UAmsterdam.A.pdf](https://trec.nist.gov/pubs/trec32/papers/UAmsterdam.A.pdf)
- :material-file-search: **Runs:** [UvA-IRLab-mlp-mlm-images](./runs.md#uva-irlab-mlp-mlm-images) | [UvA-IRLab-mlp-mlm-caption](./runs.md#uva-irlab-mlp-mlm-caption) | [UvA-IRLab-mlp-mlm-cap1](./runs.md#uva-irlab-mlp-mlm-cap1) | [UvA-IRLab-mlp-mlm-img_cap](./runs.md#uva-irlab-mlp-mlm-img_cap)

??? abstract "Abstract"
	
	Learned Sparse Retrieval (LSR) is a group of neural methods de-signed to encode queries and documents into sparse lexical vectors.These vectors can be efficiently indexed and retrieved using aninverted index. While LSR has shown promise in text retrieval,its potential in multi-modal retrieval remains largely unexplored.Motivated by this, in this work we explore the application of LSRin the multi-modal domain, i.e., we focus on Multi-Modal LearnedSparse Retrieval (MLSR). We conduct experiments using severalMLSR model configurations and evaluate the performance on theimage suggestion task. We find that solving the task solely basedon the image content is challenging. Enriching the image contentwith its caption improves the model’s performance significantly,implying the importance of image captions to provide fine-grainedconcepts and context information of images. Our approach presentsa practical and effective solution for training LSR retrieval modelsin multi-modal settings.ACM Reference Format:Nguyen, Hendriksen, Yates. 2023. Multimodal Learned Sparse Retrieval forImage Suggestion Task. In Proceedings of (TREC 2023). ACM, New York, NY,USA, 5 pages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenHY23.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenHY23,
		author = {Thong Nguyen and Mariya Hendriksen and Andrew Yates},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Multimodal Learned Sparse Retrieval for Image Suggestion Task},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/UAmsterdam.A.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenHY23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

